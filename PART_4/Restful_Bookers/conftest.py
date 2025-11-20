import pytest
import requests
from faker import Faker
from constants import HEADERS, AUTH_URL

faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)

    response = requests.post(
        AUTH_URL,
        headers=HEADERS,
        json={"username": "admin", "password": "password123"}
    )
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    assert token is not None, "В ответе не оказалось токена"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": "Cigars"
    }


@pytest.fixture
def not_full_data():
    return {
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Cigars"
    }

@pytest.fixture
def wrong_format_data():
    return {
        "firstname": faker.random_int(),
        "lastname": faker.random_int(),
        "totalprice": "100",
        "depositpaid": "",
        "bookingdates": {
            "checkin": faker.date(),
            "checkout": faker.date()
        },
        "additionalneeds": faker.random_int()
    }

@pytest.fixture
def empty_data():
    return {
        "firstname": "" ,
        "lastname": "",
        "totalprice": 0,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "",
            "checkout": ""
        },
        "additionalneeds": ""
    }