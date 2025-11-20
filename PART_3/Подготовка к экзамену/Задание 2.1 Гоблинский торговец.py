# **Тема:** Методы класса, статические методы, операции с золотом
#
# 1. Создайте класс `GoblinMerchant` с атрибутом экземпляра `gold`.
# 2. Добавьте статический метод `tax_rate()`, возвращающий 0.1 (10% налог).
# 3. Добавьте метод класса `from_rich_merchant(cls)`, создающий торговца с 1000 золота.
# 4. Реализуйте метод `buy_item(item_name, item_price)`:
#     - Проверяет, достаточно ли золота.
#     - Если достаточно: уменьшает золото на `item_price + item_price * tax_rate()`.
#     - Возвращает сообщение о покупке.
#     - Если золота не хватает, возвращает "Недостаточно золота!".
# 5. Протестируйте класс:
#     - Создайте обычного торговца с 200 золота и попробуйте купить предмет за 150.
#     - Создайте торговца через `from_rich_merchant()` и купите предмет за 500.


class GoblinMerchant:
    def __init__(self, gold):
        self.gold = gold

    @staticmethod
    def tax_rate():
        return 0.1

    @classmethod
    def from_rich_merchant(cls):
        return cls(1000)


    def buy_item(self, item_name, item_price):
        price_with_tax = item_price + item_price * self.tax_rate()
        if price_with_tax <= self.gold:
            self.gold -= price_with_tax
            return f'Вы успешно приобрели {item_name} за {price_with_tax} золота, сумма налога составила {price_with_tax - item_price}'
        else:
            return 'Недостаточно золота!'


merchant = GoblinMerchant(200)
print(merchant.buy_item("Амулет удачи", 150))  # Ожидается успешная покупка или недостаток золота
rich_merchant = GoblinMerchant.from_rich_merchant()
print(rich_merchant.buy_item("Волшебный посох", 500))  # Ожидается успешная покупка

