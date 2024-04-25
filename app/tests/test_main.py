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
