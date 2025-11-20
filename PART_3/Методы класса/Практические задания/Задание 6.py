# Создайте класс `BankAccount` для банковского счета с продвинутой логикой:
#
# **Атрибуты:**
#
# - `account_number` - номер счета (только для чтения после создания)
# - `balance` - баланс счета
# - `owner_name` - имя владельца
# - `is_active` - активен ли счет
#
# **Свойства только для чтения:**
#
# - `formatted_balance` - баланс в формате "1234 ₽"
# - `transaction_history` - история всех операций
# - `account_info` - краткая информация о счете

# **Правила валидации:**
#
# - `balance` не может быть отрицательным
# - `owner_name` должно быть непустой строкой без цифр (вот тут надо погуглить 🙂)
# - Операции возможны только если `is_active = True`
#- При каждом изменении баланса записывать операцию в историю
#
# **Дополнительные методы:**
#
# - `deposit(amount)` - пополнение счета
# - `withdraw(amount)` - снятие со счета (с проверкой достаточности средств)

class BankAccount:
    RUS_LETTERS = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
    def __init__(self, account_number, owner_name, balance, is_active = True):
        self.check_balance(balance)
        self.check_name(owner_name)

        self._account_number = account_number
        self._balance = balance
        self._owner_name = owner_name
        self._is_active = is_active
        self._transaction_history = {}
        self._deposit_count = 0
        self._withdraw_count = 0

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value

    @property
    def transaction_history(self):
        return self._transaction_history

    @classmethod
    def check_balance(cls, balance):
        balance = int(balance)
        if balance < 0:
            raise ValueError(f'Баланс должен быть положительным! Сейчас ваш баланс {balance} руб.')

    @classmethod
    def check_name(cls, owner_name):
        name = owner_name.split()
        if len(name) < 2:
            raise TypeError('В имени должен быть хотя бы 1 символ')
        for l in name:
            if len(l.strip(cls.RUS_LETTERS)) != 0:
                raise TypeError('В имени должны присутствовать только буквы русского алфавита!')

    @property
    def formatted_balance(self):
        return f'{self._balance} ₽'

    @property
    def account_info(self):
        return f'Номер счета: {self._account_number}, Имя владельца: {self._owner_name}, Баланс: {self._balance}, Счёт активен: {"Да" if self._is_active else "Нет"}'


    def deposit(self, amount):
        if self._is_active:
            self._balance += amount
            self._deposit_count += 1
            self._transaction_history['Пополнение_' + str(self._deposit_count)] = amount
        else:
            print('Ваш счёт заблокирован, обратитесь в банк')


    def withdraw(self, amount):
        if self._is_active:
            if self._balance >= amount:
                self._balance -= amount
                self._withdraw_count += 1
                self._transaction_history['Списание_' + str(self._withdraw_count)] = amount
            else:
                print(f'Запрашиваемая сума {amount} ₽ больше вашего баланса {self.formatted_balance}')
        else:
            print('Ваш счёт заблокирован, обратитесь в банк')



account = BankAccount("12345", "Иван Петров", 1000)
print(account.formatted_balance)    # "1000 ₽"
print(account.account_info)         # Краткая информация

account.deposit(500)
account.deposit(700)
account.withdraw(200)
account.withdraw(1700)
print(account.balance)              # 300
print(account.transaction_history)  # История операций# Попробуйте разные ошибки:
account.withdraw(1700)              # Ошибка
account.is_active = False
account.deposit(100)                # Ошибка - счет неактивен
# account.balance = -100            # Ошибка
#account.owner_name = "Иван123"     # Ошибка
