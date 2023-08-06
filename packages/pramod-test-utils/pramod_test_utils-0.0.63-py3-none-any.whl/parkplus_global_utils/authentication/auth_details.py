import datetime
from parkplus_global_utils.authentication.config import CONFIG
from parkplus_global_utils.authentication import token_utils
from parkplus_global_utils.authentication.raise_exception import raise_exception


class Authentication:
    def __init__(self, data, *args, **kwargs):

        request = args[0]

        self.client_id = request.headers.get("client-id", None)
        self.client_secret = request.headers.get("client-secret", None)
        self.organisation_id = request.headers.get("organisation-id", None)
        self.jwt_authorization_token = request.headers.get("authorization", None)
        self.device_id = request.headers.get("device-id", None)
        self.version_name = request.headers.get("version-name", None)
        self.version_code = request.headers.get("version-code", None)
        self.platform = request.headers.get("platform", None)
        self.x_api_key = request.headers.get("x-api-key", None)
        self.jwt_token_util = token_utils.JWTToken()
        self.payload = None
        self.parsed_payload = None

    def validate_client_credentials(self, client_id, client_secret, django_exception):
        if not self.client_id or not self.client_secret or not (
            self.client_id == client_id
            and self.client_secret == client_secret
        ):
            error_response = CONFIG.GENERIC.UNAUTHORIZED
            raise_exception(error_response, django_exception)

    def validate_authentication_token(self, jwt_secret_key, jwt_token_key, django_exception):
        if not self.jwt_authorization_token:
            error_response = CONFIG.GENERIC.UNAUTHORIZED
            raise_exception(error_response, django_exception)

        self.decode_authentication_token(jwt_secret_key, jwt_token_key, django_exception)

    def decode_authentication_token(self, jwt_secret_key, jwt_token_key, django_exception):
        if self.jwt_authorization_token:
            self.parsed_payload = self.jwt_token_util.parse_jwt_token(self.jwt_authorization_token, jwt_secret_key, django_exception)
            self.validate_parsed_payload(django_exception)
            self.payload = self.jwt_token_util.decode_jwt_token_payload(self.parsed_payload, jwt_token_key, django_exception)

    def check_role_access(self, django_exception, allowed_roles=[]):
        role = self.payload.get("role")

        # Todo : test role accessibility (testing left)
        if (
            len(allowed_roles)
            and role
            and role not in allowed_roles
            #and not settings.ENV == "LOCAL"
            #and not role == Constant.ROLES.SUPER_ADMIN[0] # todo handle this part for every service
        ):
            error_response = CONFIG.GENERIC.UNAUTHORIZED
            raise_exception(error_response, django_exception)

    def validate_parsed_payload(self, django_exception):
        if not self.parsed_payload:
            error_response = CONFIG.GENERIC.UNAUTHORIZED
            raise_exception(error_response, django_exception)

        if self.parsed_payload.get("exp"):  # and settings.ENVIRONMENT == "config.production":
            self.check_token_expiry(self.parsed_payload.get("exp"), django_exception)

    def check_token_expiry(self, expiry, django_exception):
        if datetime.datetime.fromtimestamp(expiry) <= datetime.datetime.now():
            error_response = CONFIG.GENERIC.TOKEN_EXPIRY
            raise_exception(error_response, django_exception)

    def validate_service_credentials(self, x_api_key, django_exception):
        if not self.x_api_key:
            error_response = CONFIG.GENERIC.UNAUTHORIZED
            raise_exception(error_response, django_exception)

        if not self.x_api_key == x_api_key:
            error_response = CONFIG.GENERIC.UNAUTHORIZED
            raise_exception(error_response, django_exception)
