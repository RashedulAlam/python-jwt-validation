import requests
import jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timezone


def verify_jwt(authorization_header):
    jwt_token = authorization_header.split(' ')[1]

    decoded_jwt = jwt.decode(jwt_token, options={"verify_signature": False})
    jwt_header = decoded_jwt['header']
    jwt_payload = decoded_jwt['payload']

    if 'x5u' in jwt_header:
        x5u_url = jwt_header['x5u']
        certificate_response = requests.get(x5u_url)
        certificate_pem = certificate_response.text

        certificate = load_pem_x509_certificate(
            certificate_pem.encode(), default_backend())

        jwt_algorithm = jwt_header['alg']

        try:
            jwt.decode(jwt_token, certificate.public_key(),
                       algorithms=[jwt_algorithm])

        except jwt.InvalidSignatureError:
            return False, "Invalid JWT signature"
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