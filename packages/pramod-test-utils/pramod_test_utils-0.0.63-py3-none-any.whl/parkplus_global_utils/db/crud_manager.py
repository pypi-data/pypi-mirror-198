import re
from typing import Any, Callable, Dict, List

from .basic_utils import BasicUtils
from .abs_orm_db import AbsOrmDB


class CrudController(BasicUtils):
    """
    Superclass to perform specific CRUD operations on different objects, like:

    1. CreateVehicleController
    2. UpdateVehicleController

    """

    def __init__(self, db_manager, operation):
        super().__init__()
        self.db_manager: AbsOrmDB = db_manager
        self.operation: Callable[[*Any], Any] = operation
        self.observers: List[Callable] = []

    def start(self, **kwargs):
        self.validate_input(**kwargs)

        result = self.operation(**kwargs)

        self._notify_observers(result=result, kwargs=kwargs)

        return result

    def validate_input(self, **kwargs):
        validator_names = [
            attr_name
            for attr_name in self.__dir__()
            if attr_name.startswith("validate_") and attr_name != self.validate_input.__name__
        ]

        for name in validator_names:
            validator = getattr(self, name)
            key_name = re.match(r"validate_(.*)", name).group(1)
            input_val = kwargs.get(key_name)
            validator(input_val)

    def register_observer(self, func: Callable[[Any, Dict], Any]):
        self.observers.append(func)

    def _notify_observers(self, result, kwargs):
        for observer in self.observers:
            try:
                observer(result, kwargs)
            except Exception as e:
                self.logger.info(f"Error in observer({observer.__name__}): {e}")


class CreateObjectController(CrudController):
    def __init__(self, db_manager):
        super().__init__(db_manager, operation=self.create)

    def create(self, payload: dict = None, obj=None):
        if obj is not None:
            created_obj = self.db_manager.save(obj)

        elif payload is not None:
            created_obj = self.db_manager.create(**payload)

        else:
            raise AttributeError("Either of `obj` or `payload` is required")

        return created_obj


class UpdateObjectController(CrudController):
    def __init__(self, db_manager):
        super().__init__(db_manager, operation=self.update)

    def update(self, updates: dict, obj=None, filters: dict = None, qs=None):
        if (obj is None) and (filters is None) and (qs is None):
            raise AttributeError("Either of `obj`, `qs` or `filters` is required")

        if obj:
            for k, v in updates.items():
                setattr(obj, k, v)

            self.db_manager.save(obj)
            result = [obj.id]

        else:
            filters = filters if filters else {}
            result = self.db_manager.update(filters=filters, qs=qs, **updates)

        return list(result)

    @staticmethod
    def validate_updates(updates):
        if not updates:
            raise Exception("`updates` cannot be empty")

    def validate_qs(self, qs):
        if qs and qs.model != self.db_manager.model:
            raise Exception(f"queryset is not of model `{self.db_manager.model.__name__}`")


class DeleteObjectController(CrudController):
    def __init__(self, db_manager):
        super().__init__(db_manager, operation=self.delete)

    def delete(self, obj=None, filters: dict = None):
        if obj is not None:
            delete_filters = {"id": obj.id}

        elif filters is not None:
            delete_filters = filters

        else:
            raise AttributeError("Either of `obj` or `filters` is required")

        return self.db_manager.delete(**delete_filters)


class GetObjectController(CrudController):
    def __init__(self, db_manager):
        super().__init__(db_manager, operation=self.get)

    def get(self, filters: dict, allow_inactive: bool = False, select_for_update=False):
        return self.db_manager.get(allow_inactive=allow_inactive, select_for_update=select_for_update, **filters)


class ListObjectsController(CrudController):
    def __init__(self, db_manager):
        super().__init__(db_manager, operation=self.list)

    def list(
        self, filters: dict, q, allow_inactive: bool, exclude: dict, order_by: List[str], obj_index: int = None
    ):
        result = (
            self.db_manager.list(allow_inactive=allow_inactive, q=q, **filters).exclude(**exclude).order_by(*order_by)
        )

        if obj_index == 0:
            result = result.first()
        elif obj_index == -1:
            result = result.last()

        return result


class RawQueryController(CrudController):
    def __init__(self, db_manager):
        super().__init__(db_manager, operation=self.raw)

    def raw(self, query_str: str, query_params: List[Any] = None):
        return self.db_manager.raw(query_str=query_str, query_params=query_params)


class CrudManager(BasicUtils):
    """
    Superclass to implement CRUD manager for any object. Instances of this class will act as the entry points for CRUD
    operations on specified objects. Composed of specific controllers for each CRUD operation which are hidden to the
    outer world.
    """

    def __init__(self):
        super().__init__()

        self.create_controller: CreateObjectController or None = None
        self.get_controller: GetObjectController or None = None
        self.update_controller: UpdateObjectController or None = None
        self.delete_controller: DeleteObjectController or None = None
        self.list_controller: ListObjectsController or None = None
        self.raw_controller: RawQueryController or None = None

    def create(self, payload: dict = None, obj=None):
        if isinstance(self.create_controller, CreateObjectController):
            return self.create_controller.start(payload=payload, obj=obj)
        else:
            raise NotImplementedError

    def get(self, allow_inactive: bool = False, select_for_update=False, **filters):
        if isinstance(self.get_controller, GetObjectController):
            return self.get_controller.start(allow_inactive=allow_inactive, filters=filters, select_for_update=select_for_update)
        else:
            raise NotImplementedError

    def update(self, updates: dict, obj=None, filters: dict = None, qs=None):
        if isinstance(self.update_controller, UpdateObjectController):
            return self.update_controller.start(filters=filters, obj=obj, updates=updates, qs=qs)
        else:
            raise NotImplementedError

    def delete(self, obj=None, filters: dict = None) -> List[int]:
        if isinstance(self.delete_controller, DeleteObjectController):
            return self.delete_controller.start(obj=obj, filters=filters)
        else:
            raise NotImplementedError

    def bulk_create(self):
        raise NotImplementedError

    def list(
        self,
        allow_inactive: bool = False,
        q= None,
        exclude: dict = None,
        order_by: List[str] = None,
        obj_index: int = None,
        **filters,
    ):
        if exclude is None:
            exclude = {}

        if order_by is None:
            order_by = []

        if isinstance(self.list_controller, ListObjectsController):
            return self.list_controller.start(
                allow_inactive=allow_inactive,
                q=q,
                filters=filters,
                exclude=exclude,
                order_by=order_by,
                obj_index=obj_index,
            )
        else:
            raise NotImplementedError

    def bulk_update(self):
        raise NotImplementedError

    def bulk_delete(self):
        raise NotImplementedError

    def hard_delete(self):
        raise NotImplementedError

    def get_or_create(self, defaults: dict = None, allow_inactive: bool = False, select_for_update: bool = False, **filters: dict):
        if isinstance(self.create_controller, CreateObjectController) and isinstance(
            self.get_controller, GetObjectController
        ):
            obj = self.get(allow_inactive=allow_inactive, select_for_update=select_for_update, **filters)

            if obj is None:
                temp_payload = filters

                if defaults:
                    temp_payload.update(defaults)

                payload = {k: v for k, v in temp_payload.items() if "__" not in k}
                obj = self.create(payload=payload)

                if select_for_update:
                    obj = self.get(id=obj.id, select_for_update=select_for_update)

                created = True

            else:
                created = False

            return obj, created

        else:
            raise NotImplementedError

    def update_or_create(self, defaults: dict = None, allow_inactive: bool = False, **filters: dict):
        if isinstance(self.create_controller, CreateObjectController) and isinstance(
                self.update_controller, UpdateObjectController) and isinstance(
            self.get_controller, GetObjectController
        ):
            obj = self.get(**filters, allow_inactive=allow_inactive)

            if obj:
                self.update(obj=obj, updates=defaults)
                created = False
            else:
                create_payload = {**filters, **defaults}
                obj = self.create(payload=create_payload)
                created = True

            return obj, created

        else:
            raise NotImplementedError

    def raw(self, query_str: str, query_params: List[Any] = None):
        if isinstance(self.raw_controller, RawQueryController):
            return self.raw_controller.start(query_str=query_str, query_params=query_params)
        else:
            raise NotImplementedError


def create_crud_manager(db_manager):
    crud_manager = CrudManager()

    crud_manager.create_controller = CreateObjectController(db_manager=db_manager)
    crud_manager.update_controller = UpdateObjectController(db_manager=db_manager)
    crud_manager.delete_controller = DeleteObjectController(db_manager=db_manager)
    crud_manager.get_controller = GetObjectController(db_manager=db_manager)
    crud_manager.list_controller = ListObjectsController(db_manager=db_manager)
    crud_manager.raw_controller = RawQueryController(db_manager=db_manager)

    return crud_manager
