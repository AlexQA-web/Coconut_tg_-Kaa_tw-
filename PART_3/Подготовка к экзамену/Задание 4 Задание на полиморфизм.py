# 1. Создайте классы `Peon` и `Knight`, которые:
#     - Имеют метод `work`:
#         - У `Peon` метод возвращает "Собирает золото".
#         - У `Knight` метод возвращает "Сражается с врагами".
# 2. Напишите функцию `daily_work`, которая принимает объект героя и вызывает его метод `work`.
# 3. Протестируйте с обоими классами.

class Peon:
    def work(self):
        return 'Собирает золото'

class Knight:
    def work(self):
        return 'Сражается с врагами'

def daily_work(object):
    print(object.work())

peon = Peon()
knight = Knight()

daily_work(peon)   # Вывод: Собирает золото
daily_work(knight) # Вывод: Сражается с врагами