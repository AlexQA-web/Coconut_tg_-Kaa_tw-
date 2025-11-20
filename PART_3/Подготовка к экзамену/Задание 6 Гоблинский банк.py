# 1. Создайте класс `GoblinBank`, который:
#     - Имеет приватный атрибут `__gold`, содержащий количество золота у клиента.
#     - В конструкторе принимает начальное количество золота и устанавливает его в `__gold`.
#     Если переданное значение отрицательное, выдает ошибку.
# 2. Реализуйте методы:
#     - `get_gold()` — возвращает текущее количество золота.
#     - `deposit_gold(amount)` — добавляет указанное количество золота, если оно больше 0.
#     - `withdraw_gold(amount)` — уменьшает количество золота, если сумма не превышает доступное золото.
#     Если золота недостаточно, выводит сообщение: "Недостаточно золота!".


class GoblinBank:
    def __init__(self, gold):
        if gold < 0:
            print('Золота не может быть меньше ноля!')
            self.__gold = 0
        else:
            self.__gold = gold

    def get_gold(self):
        return  self.__gold

    def deposit_gold(self, amount):
        if amount > 0:
            self.__gold += amount
            print(f'Добавлено {amount} золота, текущий баланс {self.__gold} золота')
        else:
            print('Сумма должна быть больше 0!')

    def withdraw_gold(self, amount):
        if amount > self.__gold:
            print('Недостаточно золота!')
        else:
            self.__gold -= amount
            print(f'Снято {amount} золота. Текущий баланс: {self.__gold}')


bank = GoblinBank(100)

print(bank.get_gold())  # Вывод: 100
bank.deposit_gold(50)   # Вывод: Добавлено 50 золота. Текущий баланс: 150
bank.withdraw_gold(30)  # Вывод: Снято 30 золота. Текущий баланс: 120
bank.withdraw_gold(200) # Вывод: Недостаточно золота!


