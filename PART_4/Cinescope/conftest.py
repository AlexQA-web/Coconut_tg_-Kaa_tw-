import pytest
import requests
from utils.data_generator import DataGenerator
from PART_4.Cinescope.constants import HEADERS, LOGIN_URL, REGISTER_URL

@pytest.fixture(scope="session")
def test_user():
    random_email = DataGenerator.get_random_email()
    random_name = DataGenerator.get_random_name()
    random_password = DataGenerator.get_random_password()

    return {
        "email": random_email,
        "fullName": random_name,
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": ["USER"]
    }

@pytest.fixture(scope="session")
def auth_session(test_user):
    #Регистрируем нового пользователя
    response = requests.post(REGISTER_URL, json=test_user, headers=HEADERS)
    assert response.status_code == 201, 'Ошибка при регистрации пользователя!'

    #Логинимся
    login_json = {
        "email": test_user["email"],
        "password": test_user["password"]
    }
    response = requests.post(LOGIN_URL, json=login_json, headers=HEADERS)
    assert response.status_code == 200, 'Ошибка авторизации пользователя!'

    token = response.json().get("accessToken")
    assert token is not None, 'Ошибка получения токена!'

    session = requests.Session()
    session.headers.update(HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session




