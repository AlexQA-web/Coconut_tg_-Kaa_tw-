import requests


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


def test_booking_status(URL):
    # отправляем наш запрос
    response = requests.post(f'{URL}', json=data)
    assert response.status_code == 200

    id_data = response.json()
    booking_id = id_data['bookingid']
    return booking_id

def test_check_name(URL):
    booking_id = test_booking_status(URL)
    response = requests.get(f'{URL}/{booking_id}')
    data_2 = response.json()
    assert data['firstname'] == data_2['firstname']





