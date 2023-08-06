from parkplus_global_utils.authentication.user_details import UserDetails
from parkplus_global_utils.authentication.auth_details import Authentication


class GenericAuth:
    def __init__(self, client_id, client_secret, x_api_key, jwt_secret_key, jwt_token_key):
        self.client_id = client_id
        self.client_secret = client_secret
        self.x_api_key = x_api_key
        self.jwt_secret_key = jwt_secret_key
        self.jwt_token_key = jwt_token_key

    def user_authentication(self, allowed_roles=[], django_exception=True):
        def user_decorator(f):
            def wrap(data, *args, **kwargs):
                auth_class = Authentication(data, *args, **kwargs)

                auth_class.validate_client_credentials(self.client_id, self.client_secret, django_exception)
                auth_class.validate_authentication_token(self.jwt_secret_key, self.jwt_token_key, django_exception)
                auth_class.check_role_access(django_exception, allowed_roles)

                args[0].user = UserDetails(auth_class.payload)
                args[0].jwt_token = auth_class.jwt_authorization_token
                return f(data, *args, **kwargs)

            return wrap

        return user_decorator

    def service_authentication(self, django_exception=True):
        def service_decorator(f):
            def wrap(data, *args, **kwargs):
                auth_class = Authentication(data, *args, **kwargs)

                auth_class.validate_client_credentials(self.client_id, self.client_secret, django_exception)
                auth_class.validate_service_credentials(self.x_api_key, django_exception)

                args[0].user = UserDetails(args[0].data.get("user", {}))
                args[0].jwt_token = None

                return f(data, *args, **kwargs)

            wrap.__doc__ = f.__doc__
            wrap.__name__ = f.__name__

            return wrap

        return service_decorator

    """
        It validates client credentials and
        if jwt token is present it validates the token as well.
        In case of token is not present it assign the None to userDetails.
        """

    def optional_user_authentication(self, django_exception=True):
        def optional_user_decorator(f):
            def wrap(data, *args, **kwargs):
                auth_class = Authentication(data, *args, **kwargs)
                auth_class.validate_client_credentials(self.client_id, self.client_secret, django_exception)
                if auth_class.jwt_authorization_token:
                    auth_class.validate_authentication_token(self.jwt_secret_key, self.jwt_token_key, django_exception)
                    args[0].user = UserDetails(auth_class.payload)
                    args[0].jwt_token = auth_class.jwt_authorization_token
                else:
                    args[0].user = None
                    args[0].jwt_token = None

                return f(data, *args, **kwargs)

            return wrap

        return optional_user_decorator

    def client_authentication(self, django_exception=True):
        def client_decorator(f):
            def wrap(data, *args, **kwargs):

                auth_class = Authentication(data, *args, **kwargs)

                auth_class.validate_client_credentials(self.client_id, self.client_secret, django_exception)

                args[0].user = None
                args[0].jwt_token = None

                return f(data, *args, **kwargs)

            wrap.__doc__ = f.__doc__
            wrap.__name__ = f.__name__

            return wrap

        return client_decorator

    def user_or_service_authentication(self, django_exception=True):
        def user_or_service_decorator(f):
            def wrap(data, *args, **kwargs):

                auth_class = Authentication(data, *args, **kwargs)
                auth_class.validate_client_credentials(self.client_id, self.client_secret, django_exception)
                auth_class.decode_authentication_token(self.jwt_secret_key, self.jwt_token_key, django_exception)

                if auth_class.payload:
                    args[0].user = UserDetails(auth_class.payload)
                    args[0].jwt_token = auth_class.jwt_authorization_token
                else:

                    auth_class.validate_service_credentials(self.x_api_key, django_exception)

                    args[0].user = UserDetails(args[0].data.get("user", {}))
                    args[0].jwt_token = None

                return f(data, *args, **kwargs)

            wrap.__doc__ = f.__doc__
            wrap.__name__ = f.__name__

            return wrap

        return user_or_service_decorator



