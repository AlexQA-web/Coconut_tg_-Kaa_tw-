# Создайте класс GoblinTrader, который:
# Имеет атрибут gold (количество золота у игрока).
# Метод buy_item, который принимает item_name и item_price.
# Если у игрока достаточно золота, уменьшает золото на цену предмета и выводит сообщение об успешной покупке.
# Если золота не хватает, выводит сообщение: "Недостаточно золота!"
# Создайте объект GoblinTrader и протестируйте метод.

class GoblinTrader:
    def __init__(self, gold):
        self.gold = gold

    def buy_item(self, item_name, item_price):
        if item_price > self.gold:
            print('Недостаточно золота!')
        else:
            self.gold -= item_price
            print(f'Вы успешно купили {item_name} за {item_price} золота!')



trader = GoblinTrader(200)
trader.buy_item("Свиток скорости", 150)  # Вывод: Куплен Свиток скорости
trader.buy_item("Книга заклинаний", 100)  # Вывод: Недостаточно золота!