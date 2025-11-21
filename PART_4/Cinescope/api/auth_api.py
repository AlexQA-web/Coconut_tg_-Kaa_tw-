from PART_4.Cinescope.constants import REGISTER_ENDPOINT, AUTH_BASE_URL, LOGIN_ENDPOINT
from PART_4.Cinescope.custom_requester.custom_requester import CustomRequester




class AuthAPI(CustomRequester):
    """
    Класс для работы с аутентификацией.
    """

    def __init__(self, session):
        super().__init__(session=session, base_url=AUTH_BASE_URL)

    def register_user(self, user_data, expected_status=201):
        """
        Регистрация нового пользователя.
        """
        return self.send_request(
            method="POST",
            endpoint=REGISTER_ENDPOINT,
            data=user_data,
            expected_status=expected_status,
        )

    def login_user(self, login_data):
        '''
        Логин пользователя
        :param login_data:
        :return:
        '''
        url = f"{self.base_url}{LOGIN_ENDPOINT}"
        response = self.session.request("POST", url, json=login_data, headers=self.headers)

        # Логируем запрос/ответ тем же методом, что и в CustomRequester
        self.log_request_and_response(response)

        if response.status_code not in (200, 201):
            raise ValueError(
                f"Unexpected status code: {response.status_code}. Expected: 200 or 201"
            )

        return response

    def authenticate(self, user_creds):

        login_data = {
            "email": user_creds[0],
            "password": user_creds[1],
        }

        response = self.login_user(login_data).json()

        if "accessToken" not in response:
            raise KeyError("token is missing")

        token = response["accessToken"]

        self._update_session_headers(self.session, authorization="Bearer " + token)
