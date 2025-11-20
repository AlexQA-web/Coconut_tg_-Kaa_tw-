# TODO: Создай класс BankAccount с конструктором:
from locale import currency


class BankAccount:

    def __init__(self, account_number, owner_name, initial_balance = 0, currency = 'RUB', is_active = True):
        self.account_number = account_number
        self.owner_name = owner_name
        self.initial_balance = initial_balance
        self.currency = currency
        self.is_active = is_active
    pass
# account_number (обязательный)
# owner_name (обязательный)
# initial_balance (по умолчанию 0)
# currency (по умолчанию "RUB")
# is_active (по умолчанию True)

# TODO: Создай счета разными способами:

account1 = BankAccount('123-456', 'Иван Петров', currency = 'RUB', is_active = True)  # "123-456", "Иван Петров", "RUB", True, Без баланса (должен быть 0)
account2 = BankAccount('789-012', 'Мария Сидорова', 25000)  # "789-012", "Мария Сидорова"# С балансом, но без валюты (должна быть RUB)
account3 = BankAccount('345-678', 'Петр Иванов', 23000, )  # "345-678", "Петр Иванов", 25000, Используй именованные параметры
account4 = BankAccount(account_number="999-888", owner_name="Анна Козлова", currency="USD")  # account_number="999-888", owner_name="Анна Козлова", currency="USD"

# Проверь результаты:
accounts = [account1, account2, account3, account4]
for acc in accounts:
    print(f"Счет: {acc.account_number} {acc.owner_name}")
    print(f"  Баланс: {acc.initial_balance} {acc.currency}, Активен: {acc.is_active}")