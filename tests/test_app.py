import random

import faker

fake = faker.Faker()


def test_create_user(test_client):
    post_data = {
        "full_name": fake.name(),
        "location": {
            "lat": float(fake.latitude()),
            "lon": float(fake.longitude()),
        },
    }

    response = test_client.post("/user", json=post_data)
    assert response.status_code == 200
    assert "user_id" in response.json()


def test_get_user_as_admin(test_client, admin_token, db_users):
    user = random.choice(db_users)
    response = test_client.get(f"/user/{user.user_id}", params={"token": admin_token})
    assert response.status_code == 200

    actual_location = response.json()["location"]
    assert actual_location["lat"] == float(user.location.lat)
    assert actual_location["lon"] == float(user.location.lon)


def test_get_user(test_client, db_users):
    user = random.choice(db_users)
    response = test_client.get(f"/user/{user.user_id}")
    assert response.status_code == 200

    actual_location = response.json()["location"]
    assert actual_location["lat"] != float(user.location.lat)
    assert actual_location["lon"] != float(user.location.lon)
