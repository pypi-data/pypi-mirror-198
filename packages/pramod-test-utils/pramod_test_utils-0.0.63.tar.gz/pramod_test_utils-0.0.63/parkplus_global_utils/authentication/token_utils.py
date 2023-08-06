import jwt
from parkplus_global_utils.authentication.config import CONFIG
from parkplus_global_utils.authentication.raise_exception import raise_exception

class JWTToken:
    def parse_jwt_token(self, jwt_token, jwt_secret_key, django_exception):
        try:
            return jwt.decode(jwt_token, jwt_secret_key)
        except Exception:
            error_response = CONFIG.GENERIC.INVALID_JWT_TOKEN
            raise_exception(error_response, django_exception)

    def decode_jwt_token_payload(self, payload, jwt_token_key, django_exception):
        try:
            return payload[jwt_token_key]
        except Exception:
            error_response = CONFIG.GENERIC.INVALID_JWT_TOKEN
            raise_exception(error_response, django_exception)
