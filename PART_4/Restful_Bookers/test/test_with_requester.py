import requests
import pytest
from PART_4.Restful_Bookers.constants import BOOKING_ENDPOINT



class TestPositiveApi:
    def test_create_booking(self, requester, booking_data, booking):
        response = requester.send_request(
            method="POST",
            endpoint=BOOKING_ENDPOINT,
            data=booking_data,
            expected_status=200
        )
        booking_id, _, _ = booking
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert response.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert response.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"

    def test_put_update_booking(self, requester, booking):
        booking_id, _, _ = booking
        update_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
            "additionalneeds": "Breakfast",
        }
        response = requester.send_request(
            method="PUT",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            data=update_data,
            expected_status=200
        )
        got = requester.send_request(
            method="GET",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status=200

        )
        assert got.json() == response.json(), 'Ошибка обновления ресурса!'

    def test_patch_update_booking(self, requester, booking):
        booking_id, _, _ = booking
        update = {
            "firstname": "Vasya",
            "lastname": "Black"
        }
        response = requester.send_request(
            method="PATCH",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            data=update,
            expected_status=200
        )
        got = requester.send_request(
            method="GET",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status=200

        )
        assert got.json() == response.json(), 'Ошибка обновления ресурса!'

    def test_delete_booking_and_get_after(self, requester, booking):
        booking_id, _, control = booking
        deleted = requester.send_request(
            method= "DELETE",
            endpoint= f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status=201
        )

        control["autodelete"] = False

        got = requester.send_request(
            method= "GET",
            endpoint= f"{BOOKING_ENDPOINT}/{booking_id}",
            expected_status= 404
        )


class TestNegativeBooking:
    # TODO Пробуем создать бронирование без полей 'firstname' и 'lastname'
    def test_not_full_data_create_booking(self,requester, not_full_data):
        response = requester.send_request(
            method="POST",
            endpoint=BOOKING_ENDPOINT,
            data=not_full_data,
            expected_status= 500
        )
    # TODO Пробуем создать бронирование с неверными типами данных в json
    def test_wrong_data_create_booking(self, requester, wrong_format_data):
        response = requester.send_request(
            method= "POST",
            endpoint= BOOKING_ENDPOINT,
            data= wrong_format_data,
            expected_status= 500
        )
    # TODO Пытаемся обновить ресурс через PATCH без токена
    def test_patch_booking_without_token(self, booking, not_full_data, unauthorized_requester):
        booking_id, _, _ = booking
        response = unauthorized_requester.send_request(
            method= "PATCH",
            endpoint= f'{BOOKING_ENDPOINT}/{booking_id}',
            data= not_full_data,
            expected_status= 403
        )
    # TODO Пытаемся обновить ресурс через PUT без токена
    def test_put_booking_without_token(self, booking, booking_data, unauthorized_requester):
        booking_id, _, _ = booking
        response = unauthorized_requester.send_request(
            method="PUT",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            data=booking_data,
            expected_status=403
        )
    # TODO Пытаемся удалить ресурс без токена
    def test_delete_booking_without_token(self, booking, booking_data, unauthorized_requester):
        booking_id, _, _ = booking
        response = unauthorized_requester.send_request(
            method="DELETE",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status= 403
        )
    # TODO Пытаемся обновить несуществующий ресурс через PUT
    def test_put_deleted_booking(self, booking, requester):
        booking_id, _, control = booking
        control["autodelete"] = False
        delete = requester.send_request(
            method="DELETE",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status=201
        )
        put = requester.send_request(
            method="PUT",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status= 400
        )
    # TODO Пытаемся получить несуществующий ресурс через GET
    def test_get_deleted_booking(self, booking, requester):
        booking_id, _, control = booking
        control["autodelete"] = False
        delete = requester.send_request(
            method="DELETE",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status=201
        )
        got = requester.send_request(
            method="GET",
            endpoint=f'{BOOKING_ENDPOINT}/{booking_id}',
            expected_status=404
        )








