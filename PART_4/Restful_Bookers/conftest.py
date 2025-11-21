import pytest
import requests
from faker import Faker

from PART_4.Restful_Bookers.constants import BOOKING_ENDPOINT
from constants import HEADERS, AUTH_ENDPOINT, BASE_URL, AUTH_URL
from custom_requester.custom_requester import Requester

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
@pytest.fixture
def booking(requester, booking_data):
    response = requester.send_request(
        method="POST",
        endpoint=BOOKING_ENDPOINT,
        data=booking_data,
        expected_status=200
    )
    booking_id = response.json()["bookingid"]
    control = {"autodelete": True}
    try:
        yield booking_id, response.json(), control
    finally:
        if control.get("autodelete", True):
            requester.send_request(
                method="DELETE",
                endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
                expected_status=201
            )

@pytest.fixture
def requester():
    session = requests.Session()
    request = Requester(session, base_url=BASE_URL)
    request.session.headers.update({"Accept": "application/json",
                              "Content-Type": "application/json"})
    request.login("admin", "password123")
    return request

@pytest.fixture
def unauthorized_requester():
    session = requests.Session()
    session.headers.update(HEADERS)
    requester = Requester(session, base_url=BASE_URL)
    return requester




