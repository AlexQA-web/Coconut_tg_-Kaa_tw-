
from faker import Faker
import pytest
import requests
from constants import AUTH_BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT
from custom_requester.custom_requester import CustomRequester
from utils.data_generator import DataGenerator
from api.api_manager import ApiManager

faker = Faker()

@pytest.fixture
def test_user():
    """
    Генерация случайного пользователя для тестов.
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return {
        "email": random_email,
        "fullName": random_name,
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": ["USER"]
    }

@pytest.fixture
def registered_user(api_manager, test_user):
    """
    Регистрация пользователя через AuthAPI и возврат его данных.
    """
    response = api_manager.auth_api.register_user(test_user)
    response_data = response.json()
    user = test_user.copy()
    user["id"] = response_data["id"]
    return user

@pytest.fixture(scope="session")
def api_manager(session):
    manager = ApiManager(session)
    admin_creds = ("api1@gmail.com", "asdqwe123Q")
    manager.auth_api.authenticate(admin_creds)
    return manager

@pytest.fixture(scope="session")
def requester():
    """
    Фикстура для создания экземпляра CustomRequester.
    """
    session = requests.Session()
    return CustomRequester(session=session, base_url=AUTH_BASE_URL)

@pytest.fixture(scope="session")
def session():
    """
    Фикстура для создания HTTP-сессии.
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()

@pytest.fixture
def movie_data():
    """
    Фикстура создания данных для создания фильма
    """
    return {
        "name": DataGenerator.generate_movie_name(),
        "imageUrl": DataGenerator.generate_movie_image_url(),
        "price": DataGenerator.generate_movie_price(),
        "description": DataGenerator.generate_movie_description(),
        "location": DataGenerator.generate_movie_location(),
        "published": DataGenerator.generate_movie_published(),
        "genreId": DataGenerator.generate_movie_genre_id(),  # тут рандом 1..5
    }

@pytest.fixture
def created_movie(api_manager, movie_data):
    """
    Фикстура для создания фильма
    """
    response = api_manager.movies_api.create_movie(movie_data)
    data = response.json()
    movie_id = data["id"]

    yield movie_id, data, movie_data

    api_manager.movies_api.delete_movie(movie_id)

@pytest.fixture
def unauthorized_api_manager():
    """
    ApiManager без авторизации
    """
    session = requests.Session()
    return ApiManager(session)



