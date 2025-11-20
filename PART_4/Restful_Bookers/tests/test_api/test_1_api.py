import requests


def test_booking_status(URL):
    # делаем словарь для отправки
    data = {
      "firstname": "Jim",
      "lastname": "Brown",
      "totalprice": 111,
      "depositpaid": True,
      "bookingdates": {
          "checkin": "2025-01-04",
          "checkout": "2025-01-15"
       },
      "additionalneeds": "Breakfast"
    }

    # отправляем наш запрос
    response = requests.post(f'{URL}', json=data)

    assert response.status_code == 200