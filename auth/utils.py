import json
import jwt
import requests
from django.conf import settings
from django.contrib.auth import authenticate


def jwt_get_username_from_payload_handler(payload):
    """
    JWT to Username converter
    """
    username = payload.get("sub").replace("|", ".")
    authenticate(remote_user=username)

    return username


def jwt_decode_token(token):
    """
    Returns decoded JWT token or raises an exception if token
    cannot be decoded
    """
    header = jwt.get_unverified_header(token)
    jwks = requests.get(f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json").json()
    public_key = None

    for jwk in jwks["keys"]:
        if jwk["kid"] == header["kid"]:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception("Public key not found.")

    issuer = f"https://{settings.AUTH0_DOMAIN}/"

    return jwt.decode(
        token, public_key, audience=settings.JWT_AUTH["JWT_AUDIENCE"], issuer=issuer, algorithms=["RS256"]
    )
