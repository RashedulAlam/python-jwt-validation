def test_read_main(client):
    response = client.get("/api/v1/check-jwt-validity")
    
    assert response.status_code == 200
    assert response.json() == {"valid": False, "reason": "Invalid request header."}
