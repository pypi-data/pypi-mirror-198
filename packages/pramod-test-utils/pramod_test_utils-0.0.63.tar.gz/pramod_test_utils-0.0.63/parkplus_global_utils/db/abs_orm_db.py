import datetime
from typing import Any, List

from .basic_utils import BasicUtils


class AbsOrmDB(BasicUtils):
    def __init__(self, model, active_field_name="active"):
        super(AbsOrmDB, self).__init__()

        self.model = model
        self.active_key = active_field_name

    def get_or_create(self, defaults=None, **kwargs):
        if self.active_key and self.active_key not in kwargs:
            kwargs[self.active_key] = True

        self.logger.info(f"defaults: {defaults}")
        self.logger.info(f"kwargs: {kwargs}")

        return self.model.objects.get_or_create(defaults=defaults, **kwargs)

    def get(self, allow_inactive=False, select_for_update=False, **filters):
        if self.active_key:
            if not allow_inactive and self.active_key not in filters:
                filters[self.active_key] = True

        self.logger.info(f"Filters: {filters}")

        try:
            if select_for_update:
                obj = self.model.objects.select_for_update().get(**filters)
            else:
                obj = self.model.objects.get(**filters)
        except self.model.DoesNotExist:
            obj = None

        return obj

    def create(self, **values):
        if self.active_key and self.active_key not in values:
            values[self.active_key] = True

        self.logger.info(f"Values: {values}")
        return self.model.objects.create(**values)

    def update(self, filters: dict, qs=None, **updates) -> List[int]:
        if "updated" not in updates:
            updates["updated"] = datetime.datetime.now()

        if qs is None and self.active_key and self.active_key not in filters:
            filters[self.active_key] = True

        self.logger.info(f"Filters: {filters}")
        self.logger.info(f"Updates: {updates}")
        self.logger.info(f"Queryset: {qs}")

        if qs is None:
            qs = self.model.objects.filter(**filters)
        else:
            qs = qs.filter(**filters)

        ids = qs.values_list("id", flat=True)

        qs.update(**updates)

        return ids

    def hard_delete(self, **filters):
        self.logger.info(f"Performing hard delete")
        self.logger.info(f"Filters: {filters}")
        return self.model.objects.filter(**filters).delete()

    def list(self, allow_inactive=False, q=None, **filters):
        if self.active_key and q is None:
            if not allow_inactive and self.active_key not in filters:
                filters[self.active_key] = True

        args: tuple = tuple()
        if q is not None:
            args = (q,)

        self.logger.info(f"listing objects")
        self.logger.info(f"Filters: {filters}")
        self.logger.info(f"args: {args}")

        result = self.model.objects.filter(*args, **filters)
        return result

    def update_or_create(self, updates, allow_inactive=False, **filters):
        self.logger.info(f"Defaults : {updates}")
        self.logger.info(f"Filters  : {filters}")

        if self.active_key:
            if self.active_key not in filters and not allow_inactive:
                filters[self.active_key] = True

        if "updated" not in updates:
            updates["updated"] = datetime.datetime.now()

        return self.model.objects.update_or_create(defaults=updates, **filters)

    def delete(self, **filters):

        self.logger.info(f"Filters for delete : {filters}")

        if self.active_key:

            self.logger.info(f"Performing soft delete")

            updates = {self.active_key: False}

            result = self.update(filters=filters, **updates)

        else:

            result = self.hard_delete(**filters)

        return result

    def raw(self, query_str: str, query_params: List[Any] = None):

        self.logger.info(f"Executing Query: {query_str}")

        self.logger.info(f"Query Params: {query_params}")

        return self.model.objects.raw(query_str, params=query_params)

    def save(self, obj):

        self.logger.info(f"Saving new vehicle object")

        if self.active_key and getattr(obj, self.active_key) is None:
            setattr(obj, self.active_key, True)

        values = {k: v for k, v in obj.__dict__.items() if not (k.startswith("_") or k.startswith("__"))}

        self.logger.info(f"Values: {values}")

        obj.save()

        return obj


def create_orm_db(model, active_field_name="active"):
    return AbsOrmDB(model=model, active_field_name=active_field_name)
