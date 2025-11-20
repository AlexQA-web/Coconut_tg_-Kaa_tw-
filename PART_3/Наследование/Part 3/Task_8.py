# **Цель:** Комплексное использование переопределения
#
# **Задача:** Создай систему банковских счетов с разными типами и комиссиями.
#
# **Требования:**
#
# 1. Базовый класс `BankAccount` с балансом и методами `deposit()`, `withdraw()`
# 2. `withdraw()` в базовом классе должен проверять достаточность средств
# 3. Дочерние классы с разными правилами:
#     - `SavingsAccount` - снятие с комиссией 1%
#     - `CheckingAccount` - бесплатное снятие до 1000₽, потом 2% комиссии
#     - `PremiumAccount` - бесплатное снятие, но минимальный баланс 10000₽

class BankAccount:
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def print_error(self):
        print(f'Ваш баланс меньше суммы снятия: Баланс - {self.balance}Руб., Запрашиваемая сумма - {amount}Руб.')


class SavingsAccount(BankAccount):
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance
        self.comission = 0.01

    def withdraw(self, amount):
        if BankAccount.withdraw(self, amount):
            self.balance -= amount + (amount * self.comission)
            return self.balance
        else:
            return self.print_error()




class CheckingAccount(BankAccount):
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance
        self.comission = 0.02
        self.no_coms_limit = 1000

    def withdraw(self, amount):
        if BankAccount.withdraw(self, amount):
            if amount > self.no_coms_limit:
                self.balance -= amount + ((amount - self.no_coms_limit) * self.comission)
                return self.balance
            else:
                self.balance -= amount
                return self.balance
        else:
            return self.print_error()


class PremiumAccount(BankAccount):
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance
        self.need_balance = 10000

    def withdraw(self, amount):
        if BankAccount.withdraw(self, amount) and self.balance >= self.need_balance:
            self.balance -= amount
            return self.balance
        else:
            return self.print_error()


# TODO: Спроектируй и реализуй всю систему
# Пример тестирования:
accounts = [
    SavingsAccount("Сберегательный", 5000),
    CheckingAccount("Расчетный", 3000),
    PremiumAccount("Премиум", 5000)
]

# Тест снятия разных сумм
for account in accounts:
    print(f"\n=== {account.account_type} счет ===")
    print(f"Баланс: {account.balance}₽")
    print(account.withdraw(500))   # Попробуй снять 500₽
    print(account.withdraw(1500))  # Попробуй снять 1500₽
    print(f"Итоговый баланс: {account.balance}₽")

