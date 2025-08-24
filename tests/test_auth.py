
def create_user(client):
    response = client.post("/users/", json={
        "username": "authuser",
        "email": "authuser@example.com",
        "full_name": "Auth User",
        "password": "password123"
    })
    return response

def test_login_success(client):
    create_user(client)
    response = client.post("/auth/login", data={
        "username": "authuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client):
    create_user(client)
    response = client.post("/auth/login", data={
        "username": "authuser@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 403
    assert response.json()["detail"] == "Invalid credentials"

def test_login_nonexistent_user(client):
    response = client.post("/auth/login", data={
        "username": "nouser@example.com",
        "password": "password123"
    })
    assert response.status_code == 403
    assert response.json()["detail"] == "Invalid credentials"