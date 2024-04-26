# FastAPI JWT Validation API

## Overview

This FastAPI API provides endpoints to validate JWT tokens from request headers.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/RashedulAlam/python-jwt-validation.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

### Local environment
To run the API locally, use the following command:

```bash
uvicorn app.main:app --reload
```

### Docker environment

To run the API using Docker, build the Docker image:

```bash
docker build -t fastapi-jwt-validation .
docker run -d --name fastapi-jwt-validation -p 8000:80 fastapi-jwt-validation
```

## Endpoints

### `/api/v1/check-jwt-validity`

#### GET

Checks JWT token validity from the request header.

- **Parameters**:

- **Returns**:
  - `valid` (bool): Whether the token is valid or not.
  - `reason` (str): Reason for token validation result.

### `/v2/check-jwt-validity`

#### GET

Checks JWT token validity from the request header with additional options.

- **Parameters**:

- **Returns**:
  - `valid` (bool): Whether the token is valid or not.
  - `reason` (str): Reason for token validation result.


## API Request and Response Samples

### `/api/v1/check-jwt-validity`

#### Request

```http
GET /api/v1/check-jwt-validity
Authorization: Bearer <VALID_JWT_TOKEN>
```
#### Response

```json
{
  "valid": true
}
```
#### Request

```http
GET /api/v1/check-jwt-validity
Authorization: Bearer <INVALID_JWT_TOKEN>
```
#### Response

```json
{
  "valid": false,
  "reason": "Invalid JWT signature"
}
```

### `/v2/check-jwt-validity`

#### Request

```http
GET /v1/check-jwt-validity
Authorization: Bearer <VALID_JWT_TOKEN>
```
#### Response

```json
{
  "valid": false
}
```

#### Request

```http
GET /v1/check-jwt-validity
Authorization: Bearer <INVALID_JWT_TOKEN_INVALID_SIGNATURE>
```
#### Response

```json
{
  "valid": false,
  "reason": "Invalid JWT signature"
}
```