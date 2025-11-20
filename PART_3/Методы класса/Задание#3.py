class BankAccount:
    def __init__(self, balance):
        self._balance = balance


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print('Сумма пополнения должна быть больше чем 0 руб.')


    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print(f'Сумма снятия {amount} превышает средства на балансе {self._balance}')

    def get_balance(self):
        print(f'Ваш баланс составляет {self._balance} руб.')
        return self._balance


account = BankAccount(1000)
account.deposit(500)
account.withdraw(2000)
print(account.get_balance())
"""Мы можем обратиться к защищенному атрибуту напрямую, но это не рекомендуется"""
print(account._balance)  # Вывод: 1500 (но лучше использовать account.get_balance())

account._balance = -1000 #можем изменить напрямую, но это плохо
print(account.get_balance()) #вывод -1000, что недопустимо
account.withdraw(100)
print(account.get_balance()) #вывод -1100, что недопустимо
