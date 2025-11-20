class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transaction_count = 0

    # TODO: Создай метод deposit(amount) - пополнение счета
    def deposit(self, amount):
        # 1. Проверь что amount больше 0
        if amount > 0:
            # 2. Увеличь self.balance на amount
            self.balance += amount
            # 3. Увеличь self.transaction_count на 1
            self.transaction_count += 1
            # 4. Выведи сообщение о пополнении
            print(f'Ваш баланс успешно поплнен на {amount} руб.')
            # 5. Верни новый баланс
            return self.balance
        else:
            return 'Сумма пополнения должна быть больше чем 0 руб.'

    # TODO: Создай метод withdraw(amount) - снятие денег
    def withdraw(self, amount):
        # 1. Проверь что amount больше 0
        if amount > 0:
            # 2. Проверь что на счету достаточно денег
            if self.balance > amount:
                # 3. Если достаточно - уменьши balance и увеличь transaction_count
                self.balance -= amount
                self.transaction_count += 1
                # 4. Выведи сообщение об операции
                print(f'Снятие {amount} руб. произошло успешно!')
                # 5. Верни True если операция успешна, False если нет
                return  True
        return False


    # TODO: Создай метод get_balance() - получение баланса
    def get_balance(self):
        # Верни текущий баланс
        return self.balance


    # TODO: Создай метод get_info() - информация о счете
    def get_info(self):
        # Верни строку с информацией: "Счет {owner_name}: {balance}₽, операций: {transaction_count}"
        return f"Счет {self.owner_name}: {self.balance}₽, операций: {self.transaction_count}"


# Тестирование:
account = BankAccount("Иван Петров", 1000)

print("Начальное состояние:")
print(account.get_info())

print("\nПополняем счет:")
new_balance = account.deposit(500)
print(f"Новый баланс: {new_balance}₽")

print("\nСнимаем деньги:")
success = account.withdraw(200)
print(f"Операция {'успешна' if success else 'неуспешна'}")

print("\nПытаемся снять больше, чем есть:")
success = account.withdraw(2000)
print(f"Операция {'успешна' if success else 'неуспешна'}")

print("\nИтоговое состояние:")
print(account.get_info())
