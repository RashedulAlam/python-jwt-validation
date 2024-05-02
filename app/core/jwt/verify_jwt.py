import requests
import jwt
from datetime import datetime, timezone
from cachetools import TTLCache
from cryptography.hazmat.primitives.serialization import load_pem_public_key

CACHE_TTL_SECONDS = 3600

certificate_cache = TTLCache(maxsize=100, ttl=CACHE_TTL_SECONDS)


def get_certificate_from_url(url):
    certificate_response = requests.get(url)

    if certificate_response.status_code != 200:
        raise requests.RequestException('Unable to load certificate')

    certificate_pem = certificate_response.text
    certificate = load_pem_public_key(certificate_pem.encode())

    return certificate


def get_certificate_from_cache(url):
    if url in certificate_cache:
        return certificate_cache[url]
    else:
        certificate = get_certificate_from_url(url)
        certificate_cache[url] = certificate

        return certificate


def verify_jwt(jwt_token, use_cache=False):
    """verifies jwt token.

    Args:
        authorization_header (string): The authorization header value.
        use_cache (boolean): Whether to use certificate loading from cache or not.

    Returns:
        Whether token is valid or not and reason.
    """

    try:
        decoded_jwt = jwt.decode(
            jwt_token, options={"verify_signature": False})

    except jwt.exceptions.DecodeError:
        return False, "Invalid JWT segements"

    except Exception:
        return False, "Unknown JWT token error"

    jwt_header = jwt.get_unverified_header(jwt_token)
    jwt_payload = decoded_jwt

    if 'x5u' in jwt_header:
        x5u_url = jwt_header['x5u']
        try:
            certificate = None

            if use_cache is True:
                certificate = get_certificate_from_cache(x5u_url)
            else:
                certificate = get_certificate_from_url(x5u_url)

            jwt_algorithm = jwt_header['alg']

            jwt.decode(jwt_token, certificate, algorithms=[jwt_algorithm])

        except jwt.InvalidSignatureError:
            return False, "Invalid JWT signature"

        except requests.exceptions.RequestException:
            return False, f"Error fetching certificate"
        
        except jwt.ExpiredSignatureError:
            return False, f"Token expired"
        
        except Exception as e:
            print(e)
            return False, f"Unknown error"

    else:
        return False, "Invalid JWT signing keys"

    if 'iat' not in jwt_payload or 'exp' not in jwt_payload:
        if 'iat' not in jwt_payload:
            return False, "Invalid JWT issue at"

        if 'exp' not in jwt_payload:
            return False, "Invalid JWT expiration exp"

    current_time = datetime.now(timezone.utc).timestamp()

    if jwt_payload['iat'] > current_time:
        return False, "JWT not yet valid"

    if jwt_payload['exp'] < current_time:
        return False, "JWT has expired"

    return True, "JWT is valid"
