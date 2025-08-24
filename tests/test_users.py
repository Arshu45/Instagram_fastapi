def test_create_user_success(client):
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "full_name": "Test User",
        "password": "password123"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"
    assert "id" in data

def test_create_user_duplicate(client):
    # First user creation
    client.post("/users/", json={
        "username": "duplicateuser",
        "email": "duplicate@example.com",
        "full_name": "Dup User",
        "password": "password123"
    })
    # Try to create with same username/email
    response = client.post("/users/", json={
        "username": "duplicateuser",
        "email": "duplicate@example.com",
        "full_name": "Dup User",
        "password": "password123"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Username or email already exists"

def test_read_user_success(client):
    # Create a user first
    create_resp = client.post("/users/", json={
        "username": "readuser",
        "email": "readuser@example.com",
        "full_name": "Read User",
        "password": "password123"
    })
    user_id = create_resp.json()["id"]
    # Read the user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "readuser"
    assert data["email"] == "readuser@example.com"

def test_read_user_not_found(client):
    response = client.get("/users/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"