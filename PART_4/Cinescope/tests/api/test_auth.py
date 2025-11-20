import requests
from PART_4.Cinescope.constants import REGISTER_URL, HEADERS


class TestAuthApi:
    def test_auth(self, test_user):
        response = requests.post(REGISTER_URL, json=test_user, headers=HEADERS)
        assert response.status_code == 201, 'Ошибка при регистрации пользователя!'

        r_data = response.json()
        assert r_data["email"] == test_user["email"], 'Электропочта не совпадает!'
        assert "id" in r_data, 'id не было передано в ответе!'
        assert "roles" in r_data, 'Роль не была передана в ответе!'
        assert "USER" in r_data["roles"], 'Роль пользователя не совпадает с USER!'
