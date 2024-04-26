from unittest.mock import Mock


def test_v1_no_token(client):
    response = client.get("/api/v1/check-jwt-validity")
    
    assert response.status_code == 200
    assert response.json() == {"valid": False, "reason": "Invalid request header"}

def test_v1_invalid_token(client):
    response = client.get("/api/v1/check-jwt-validity", headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsIng1dSI6Imh0dHBzOi8vZXhhbXBsZS5jb20vY2VydC5wZW0ifQ.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2MTM4ODQ0MDJ9.Egq3FzoKPlJ4lRyF0tF2Ug1kUThTTd-0MmlvDjAh-tvPflDpXq0YkxOKv_k4RGy7qGLK2h1fyKAg23Ijv84rd0Wdp_nU4b16Le8BX6EM"})
    
    assert response.status_code == 200
    assert response.json() == {"valid": False, "reason": "Error fetching certificate"}
    
    response = client.get("/api/v1/check-jwt-validity", headers={"Authorization": "Bearer asd"})
    
    assert response.status_code == 200
    assert response.json() == {"valid": False, "reason": "Invalid JWT segements"}
    
def test_v2_no_token(client):
    response = client.get("/api/v2/check-jwt-validity")
    
    assert response.status_code == 200
    assert response.json() == {"valid": False, "reason": "Invalid request header"}

def test_v2_invalid_token(client):
    response = client.get("/api/v2/check-jwt-validity", headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsIng1dSI6Imh0dHBzOi8vZXhhbXBsZS5jb20vY2VydC5wZW0ifQ.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2MTM4ODQ0MDJ9.Egq3FzoKPlJ4lRyF0tF2Ug1kUThTTd-0MmlvDjAh-tvPflDpXq0YkxOKv_k4RGy7qGLK2h1fyKAg23Ijv84rd0Wdp_nU4b16Le8BX6EM"})
    
    assert response.status_code == 200
    assert response.json() == {"valid": False, "reason": "Error fetching certificate"}
    
    response = client.get("/api/v2/check-jwt-validity", headers={"Authorization": "Bearer asd"})
    
    assert response.status_code == 200
    assert response.json() == {"valid": False, "reason": "Invalid JWT segements"}
    
def test_v1_valid_token(client, mock_jwt_token, mock_requests_get, mock_public_key):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = mock_public_key
    mock_requests_get.return_value = mock_response
    
    response = client.get("/api/v1/check-jwt-validity", headers={"Authorization": f"Bearer {mock_jwt_token}"})
    
    assert response.status_code == 200
    assert response.json() == {"valid": True}


def test_v2_valid_token(client, mock_jwt_token, mock_requests_get, mock_public_key):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = mock_public_key
    mock_requests_get.return_value = mock_response
    
    response = client.get("/api/v2/check-jwt-validity", headers={"Authorization": f"Bearer {mock_jwt_token}"})
    
    assert response.status_code == 200
    assert response.json() == {"valid": True}
    
    # check whether error throws or not while using cache signing keys
    
    response = client.get("/api/v2/check-jwt-validity", headers={"Authorization": f"Bearer {mock_jwt_token}"})
    
    assert response.status_code == 200
    assert response.json() == {"valid": True}

