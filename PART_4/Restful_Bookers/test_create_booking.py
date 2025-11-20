import requests
import pytest
from constants import BOOKING_URL

class TestBookings:
    def test_positive_booking(self, auth_session, booking_data):
        # Создаём бронирование
        create_booking = auth_session.post(BOOKING_URL, json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"

        #TODO Делаем update методом PUT
        update_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        update_booking = auth_session.put(f'{BOOKING_URL}/{booking_id}', json=update_data)
        assert update_booking.status_code == 200, 'Ошибка при обновлении брони'
        get_updated_booking = auth_session.get(f'{BOOKING_URL}/{booking_id}')
        assert get_updated_booking.json() == update_booking.json()

        # TODO Делаем частичный update методом PATCH
        part_data = {
            "additionalneeds": 'Breakfast && Diner'
        }
        part_update = auth_session.patch(f'{BOOKING_URL}/{booking_id}', headers=auth_session.headers, json=part_data)
        assert part_update.status_code == 200, 'Частичное обновление ресурса не выполнено'
        part_get = auth_session.get(f'{BOOKING_URL}/{booking_id}')
        assert part_data["additionalneeds"] == part_get.json().get("additionalneeds")
        assert part_get.json().get("firstname") == get_updated_booking.json().get("firstname")
        assert part_get.json().get("lastname") == get_updated_booking.json().get("lastname")
        assert part_get.json().get("totalprice") == get_updated_booking.json().get("totalprice")
        assert part_get.json().get("depositpaid") == get_updated_booking.json().get("depositpaid")
        assert part_get.json()["bookingdates"]["checkin"] == get_updated_booking.json()["bookingdates"]["checkin"]
        assert part_get.json()["bookingdates"]["checkout"] == get_updated_booking.json()["bookingdates"]["checkout"]

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f'{BOOKING_URL}/{booking_id}')
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f'{BOOKING_URL}/{booking_id}')
        assert get_booking.status_code == 404, "Бронь не удалилась"
        return booking_id

class TestNegativeBookings:
    def test_negative_bookings(self,auth_session, not_full_data, wrong_format_data, booking_data):
        # Создаём бронирование с валидными данными
        create_booking = auth_session.post(BOOKING_URL, json=booking_data)
        # Получаем id бронирования
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None

        #TODO Пробуем создать бронирование без полей 'firstname' и 'lastname'
        not_full_data_booking = auth_session.post(BOOKING_URL, json=not_full_data)
        assert not_full_data_booking.status_code == 500, "Бронирование создано!"

        #TODO Пробуем создать бронирование с неверными типами данных в json
        wrong_format_data_booking = auth_session.post(BOOKING_URL, json=wrong_format_data)
        assert wrong_format_data_booking.status_code == 500, "Бронирование создано!"

        #TODO Пытаемся обновить ресурс через PATCH без токена
        no_token_patch_booking = requests.patch(f'{BOOKING_URL}/{booking_id}', json=booking_data)
        assert no_token_patch_booking.status_code == 403, "Бронирование изменилось!"

        #TODO Пытаемся обновить ресурс через PUT без токена
        no_token_put_booking = requests.put(f'{BOOKING_URL}/{booking_id}', json=booking_data)
        assert no_token_put_booking.status_code == 403, "Бронирование изменилось!"

        #TODO Пытаемся удалить ресурс без токена
        try_delete_booking = requests.delete(f'{BOOKING_URL}/{booking_id}')
        assert try_delete_booking.status_code == 403, "Бронирование удалено!"
        # Удаляем бронирование
        deleted_booking = auth_session.delete(f'{BOOKING_URL}/{booking_id}')
        assert deleted_booking.status_code == 201, "Бронирование не удалено!"

        #TODO Пытаемся обновить несуществующий ресурс через PUT
        try_update_deleted = auth_session.put(f'{BOOKING_URL}/{booking_id}')
        assert try_update_deleted.status_code == 400, "Бронирование обновлено!"

        #TODO Пытаемся получить несуществующий ресурс через GET
        try_get_deleted = auth_session.get(f'{BOOKING_URL}/{booking_id}')
        assert try_get_deleted.status_code == 404, "Бронирование получено!"
