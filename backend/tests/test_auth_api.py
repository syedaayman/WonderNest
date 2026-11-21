"""Authentication endpoint tests: login, current user and logout."""

DEMO_PASSWORD = "Demo@12345"


def test_login_demo_student_returns_tokens_and_user(client):
    resp = client.post(
        "/api/auth/login", json={"username": "demo_student", "password": DEMO_PASSWORD}
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["access_token"]
    assert body["refresh_token"]
    assert body["user"]["role"] == "student"


def test_wrong_password_and_unknown_user_both_return_401_with_same_detail(client):
    wrong_password = client.post(
        "/api/auth/login", json={"username": "demo_student", "password": "Wrong@99999"}
    )
    unknown_user = client.post(
        "/api/auth/login", json={"username": "no_such_user", "password": "Wrong@99999"}
    )
    assert wrong_password.status_code == 401
    assert unknown_user.status_code == 401
    assert wrong_password.json()["detail"] == unknown_user.json()["detail"]


def test_me_with_valid_token_returns_demo_student(client, demo_token):
    resp = client.get("/api/auth/me", headers={"Authorization": f"Bearer {demo_token}"})
    assert resp.status_code == 200, resp.text
    assert resp.json()["username"] == "demo_student"


def test_me_without_header_returns_401(client):
    assert client.get("/api/auth/me").status_code == 401


def test_me_with_malformed_token_returns_401(client):
    resp = client.get("/api/auth/me", headers={"Authorization": "Bearer not.a.token"})
    assert resp.status_code == 401


def test_logout_with_valid_token_and_refresh_token_returns_204(client):
    login = client.post(
        "/api/auth/login", json={"username": "demo_student", "password": DEMO_PASSWORD}
    )
    assert login.status_code == 200, login.text
    access = login.json()["access_token"]
    refresh = login.json()["refresh_token"]

    resp = client.post(
        "/api/auth/logout",
        headers={"Authorization": f"Bearer {access}"},
        json={"refresh_token": refresh},
    )
    assert resp.status_code == 204
