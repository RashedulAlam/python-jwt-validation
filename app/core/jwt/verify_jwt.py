import requests
import jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timezone
from cachetools import TTLCache

CACHE_TTL_SECONDS = 3600

certificate_cache = TTLCache(maxsize=100, ttl=CACHE_TTL_SECONDS)


def get_certificate_from_url(url):
    certificate_response = requests.get(url)
    certificate_pem = certificate_response.text
    certificate = load_pem_x509_certificate(
        certificate_pem.encode(), default_backend())

    return certificate


def get_certificate_from_cache(url):
    if url in certificate_cache:
        return certificate_cache[url]
    else:
        certificate = get_certificate_from_url(url)
        certificate_cache[url] = certificate

        return certificate


def verify_jwt(authorization_header, use_cache=False):
    """verifies jwt token.

    Args:
        authorization_header (string): The authorization header value.
        use_cache (boolean): Whether to use certificate loading from cache or not.

    Returns:
        Whether token is valid or not and reason.
    """
    jwt_token = authorization_header.split(' ')[1]

    decoded_jwt = jwt.decode(jwt_token, options={"verify_signature": False})
    jwt_header = decoded_jwt['header']
    jwt_payload = decoded_jwt['payload']

    if 'x5u' in jwt_header:
        x5u_url = jwt_header['x5u']
        try:
            certificate = None

            if use_cache is True:
                certificate = get_certificate_from_cache(x5u_url)
            else:
                certificate = get_certificate_from_url(x5u_url)

            jwt_algorithm = jwt_header['alg']

            jwt.decode(jwt_token, certificate.public_key(),
                       algorithms=[jwt_algorithm])

        except jwt.InvalidSignatureError:
            return False, "Invalid JWT signature"

        except requests.exceptions.RequestException as e:
            return False, f"Error fetching certificate: {e}"

        except Exception:
            return False, f"Error Processing JWT token"
    else:
        return False, "Invalid JWT signing keys"

    if 'iat' not in jwt_payload or 'exp' not in jwt_payload:
        if 'iat' not in jwt_payload:
            return False, "Invalid JWT issue at"

        if 'exp' not in jwt_payload:
            return False, "Invalid JWT expiration at"

    current_time = datetime.now(timezone.utc).timestamp()

    if jwt_payload['iat'] > current_time:
        return False, "JWT not yet valid"

    if jwt_payload['exp'] < current_time:
        return False, "JWT has expired"

    return True, "JWT is valid"
