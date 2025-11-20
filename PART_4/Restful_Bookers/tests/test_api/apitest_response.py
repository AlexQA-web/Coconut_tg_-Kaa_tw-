import requests

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
response = requests.post(
    'https://restful-booker.herokuapp.com/booking', json=data)

print(response.json())

