# Твоя очередь сделать полностью самостоятельное проектирование с переопределением
#
# **Задача:** Создай систему отправки уведомлений. Должен быть базовый класс `Notification`
# и дочерние классы для разных типов уведомлений.
#
# **Требования:**
#
# 1. Базовый класс `Notification` с атрибутами `message` и `recipient`
# 2. Метод `send()` в базовом классе, который возвращает общее сообщение
# 3. Дочерние классы: `EmailNotification`, `SMSNotification`, `PushNotification`
# 4. Каждый дочерний класс переопределяет `send()` по-своему:
#     - Email: "Отправка email для {recipient}: {message}"
#     - SMS: "Отправка SMS на номер {recipient}: {message}"
#     - Push: "Push-уведомление для {recipient}: {message}"


class Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient

    def send(self):
        return f'Общее сообщение для {self.recipient}: {self.message}'


class EmailNotification(Notification):
    def send(self):
        return f'Отправка email для {self.recipient}: {self.message}'

class SMSNotification(Notification):
    def send(self):
        return f'Отправка SMS для {self.recipient}: {self.message}'

class PushNotification(Notification):
    def send(self):
        return f'Отправка Push для {self.recipient}: {self.message}'


notifications = [
    EmailNotification("Добро пожаловать!", "user@example.com"),
    SMSNotification("Код подтверждения: 1234", "+7-999-123-45-67"),
    PushNotification("У вас новое сообщение", "user_123"),
    Notification("Общее уведомление", "admin")  # базовый класс
]

for notification in notifications:
    print(notification.send())