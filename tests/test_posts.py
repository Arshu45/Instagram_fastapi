
def create_user(client):
    response = client.post("/users/", json={
        "username": "postuser",
        "email": "postuser@example.com",
        "full_name": "Post User",
        "password": "password123"
    })
    return response.json()

def login_user(client):
    response = client.post("/auth/login", data={
        "username": "postuser@example.com",
        "password": "password123"
    })
    return response.json()["access_token"]

def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}

def test_create_post(client):
    create_user(client)
    token = login_user(client)
    response = client.post("/posts/", json={
        "title": "Test Post",
        "description": "Test Description"
    }, headers=auth_headers(token))
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["description"] == "Test Description"
    assert "id" in data

def test_get_posts(client):
    create_user(client)
    token = login_user(client)
    # Create a post
    client.post("/posts/", json={
        "title": "Another Post",
        "description": "Another Description"
    }, headers=auth_headers(token))
    response = client.get("/posts/", headers=auth_headers(token))
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert any(post["Post"]["title"] == "Another Post" for post in posts)

def test_read_post(client):
    create_user(client)
    token = login_user(client)
    post_resp = client.post("/posts/", json={
        "title": "Read Post",
        "description": "Read Description"
    }, headers=auth_headers(token))
    post_id = post_resp.json()["id"]
    response = client.get(f"/posts/{post_id}", headers=auth_headers(token))
    assert response.status_code == 200
    data = response.json()
    assert data["Post"]["title"] == "Read Post"
    assert data["votes"] == 0

def test_update_post(client):
    create_user(client)
    token = login_user(client)
    post_resp = client.post("/posts/", json={
        "title": "Old Title",
        "description": "Old Description"
    }, headers=auth_headers(token))
    post_id = post_resp.json()["id"]
    response = client.put(f"/posts/{post_id}", json={
        "title": "New Title",
        "description": "New Description"
    }, headers=auth_headers(token))
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["description"] == "New Description"

def test_delete_post(client):
    create_user(client)
    token = login_user(client)
    post_resp = client.post("/posts/", json={
        "title": "Delete Me",
        "description": "Delete Description"
    }, headers=auth_headers(token))
    post_id = post_resp.json()["id"]
    response = client.delete(f"/posts/{post_id}", headers=auth_headers(token))
    assert response.status_code == 204
    # Confirm deletion
    get_resp = client.get(f"/posts/{post_id}", headers=auth_headers(token))
    assert get_resp.status_code == 404

def test_update_post_unauthorized(client):
    create_user(client)
    token = login_user(client)
    post_resp = client.post("/posts/", json={
        "title": "Unauthorized Update",
        "description": "Should Fail"
    }, headers=auth_headers(token))
    post_id = post_resp.json()["id"]
    # Create another user
    client.post("/users/", json={
        "username": "otheruser",
        "email": "otheruser@example.com",
        "full_name": "Other User",
        "password": "password123"
    })
    other_token_resp = client.post("/auth/login", data={
        "username": "otheruser@example.com",
        "password": "password123"
    })
    other_token = other_token_resp.json()["access_token"]
    response = client.put(f"/posts/{post_id}", json={
        "title": "Hacked",
        "description": "Hacked"
    }, headers=auth_headers(other_token))
    assert response.status_code == 403

def test_delete_post_unauthorized(client):
    create_user(client)
    token = login_user(client)
    post_resp = client.post("/posts/", json={
        "title": "Unauthorized Delete",
        "description": "Should Fail"
    }, headers=auth_headers(token))
    post_id = post_resp.json()["id"]
    # Create another user
    client.post("/users/", json={
        "username": "otheruser2",
        "email": "otheruser2@example.com",
        "full_name": "Other User2",
        "password": "password123"
    })
    other_token_resp = client.post("/auth/login", data={
        "username": "otheruser2@example.com",
        "password": "password123"
    })
    other_token = other_token_resp.json()["access_token"]
    response = client.delete(f"/posts/{post_id}", headers=auth_headers(other_token))
    assert response.status_code == 403