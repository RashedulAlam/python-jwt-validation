from datetime import datetime, timedelta, timezone
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import jwt
import os


def generate_token(url):

    with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
    }

    certificate = load_pem_private_key(
        private_certificate_content.encode(), os.getenv('PRIVATE_KEY_PASSOWRD').encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x5u": f'{url.scheme}://{url.hostname}:{url.port}/api/v1/signing-keys/cert'})

    return signed_token


def generate_invalid_cert_token(url):

    with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
    }

    certificate = load_pem_private_key(
        private_certificate_content.encode(), os.getenv('PRIVATE_KEY_PASSOWRD').encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x5u": f'{url.scheme}://{url.hostname}:{url.port}/api/v1/signing-keys/cert-invalid'})

    return signed_token


def generate_expired_token(url):

    with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": int((datetime.now(timezone.utc) - timedelta(hours=3)).timestamp()),
        "exp": int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp())
    }

    certificate = load_pem_private_key(
        private_certificate_content.encode(), os.getenv('PRIVATE_KEY_PASSOWRD').encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x5u": f'{url.scheme}://{url.hostname}:{url.port}/api/v1/signing-keys/cert'})

    return signed_token


def generate_invalid_header_token(url):

    with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": int((datetime.now(timezone.utc) - timedelta(hours=3)).timestamp()),
        "exp": int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp())
    }

    certificate = load_pem_private_key(
        private_certificate_content.encode(), os.getenv('PRIVATE_KEY_PASSOWRD').encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x55u": f'{url.scheme}://{url.hostname}:{url.port}/api/v1/signing-keys/cert'})

    return signed_token


def generate_invalid_payload_at_token(url):

    with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "exp": int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp())
    }

    certificate = load_pem_private_key(
        private_certificate_content.encode(), os.getenv('PRIVATE_KEY_PASSOWRD').encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x5u": f'{url.scheme}://{url.hostname}:{url.port}/api/v1/signing-keys/cert'})

    return signed_token

def generate_invalid_payload_exp_token(url):

    with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": int((datetime.now(timezone.utc) - timedelta(hours=3)).timestamp()),
    }

    certificate = load_pem_private_key(
        private_certificate_content.encode(), os.getenv('PRIVATE_KEY_PASSOWRD').encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x5u": f'{url.scheme}://{url.hostname}:{url.port}/api/v1/signing-keys/cert'})

    return signed_token
