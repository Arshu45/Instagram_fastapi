
def create_user_and_login(client, username="voteuser", email="voteuser@example.com"):
    client.post("/users/", json={
        "username": username,
        "email": email,
        "full_name": "Vote User",
        "password": "password123"
    })
    resp = client.post("/auth/login", data={
        "username": email,
        "password": "password123"
    })
    token = resp.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def create_post(client, headers):
    resp = client.post("/posts/", json={
        "title": "Vote Post",
        "description": "Vote Description"
    }, headers=headers)
    return resp.json()["id"]

def test_vote_add_and_remove(client):
    headers = create_user_and_login(client)
    post_id = create_post(client, headers)
    # Add vote
    resp = client.post("/vote/", json={"post_id": post_id, "direction": 1}, headers=headers)
    assert resp.status_code == 201
    assert resp.json()["message"] == "Vote added"
    # Remove vote
    resp = client.post("/vote/", json={"post_id": post_id, "direction": 0}, headers=headers)
    assert resp.status_code == 201
    assert resp.json()["message"] == "Vote removed"

def test_vote_duplicate(client):
    headers = create_user_and_login(client)
    post_id = create_post(client, headers)
    # Add vote
    client.post("/vote/", json={"post_id": post_id, "direction": 1}, headers=headers)
    # Try to vote again
    resp = client.post("/vote/", json={"post_id": post_id, "direction": 1}, headers=headers)
    assert resp.status_code == 409
    assert resp.json()["detail"] == "You have already voted on this post"

def test_remove_vote_not_found(client):
    headers = create_user_and_login(client)
    post_id = create_post(client, headers)
    # Try to remove vote without voting first
    resp = client.post("/vote/", json={"post_id": post_id, "direction": 0}, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Vote not found"

def test_vote_post_not_found(client):
    headers = create_user_and_login(client)
    # Try to vote on a non-existent post
    resp = client.post("/vote/", json={"post_id": 999999, "direction": 1}, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Post not found"

def test_vote_invalid_direction(client):
    headers = create_user_and_login(client)
    post_id = create_post(client, headers)
    # Try invalid direction
    resp = client.post("/vote/", json={"post_id": post_id, "direction": 2}, headers=headers)
    assert resp.status_code == 422
    assert resp.json()["detail"] == "Invalid vote direction"