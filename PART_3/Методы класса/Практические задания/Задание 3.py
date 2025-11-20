
# Создайте класс `User` с атрибутами `username` и `email`. Затем **специально** вызовите следующие ошибки
# и прочитайте их сообщения:
#
# **3.1.** Получите ошибку `AttributeError: can't set attribute`
#
# - создайте свойство только с геттером и попробуйте что-то в него записать
#
# **3.2.** Получите ошибку `TypeError: ... takes ... positional arguments but ... were given`
#
# - неправильное количество параметров в сеттере
#
# **3.3.** Получите ошибку при попытке создать сеттер без геттера

# TODO: Получите ошибку `AttributeError: can't set attribute`
class Example:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


#e = Example(12)
#e.value = 15

# TODO: **3.2.** Получите ошибку `TypeError: ... takes ... positional arguments but ... were given`
class Example_1:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def coord(self):
        return self._x, self._y

    @coord.setter
    def coord(self, x, y):
        self._x = x
        self._y = y

# e = Example_1(16, 55)
# e.coord = 11
# print(e.coord)

# TODO: **3.3.** Получите ошибку при попытке создать сеттер без геттера

class Example_2:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @coord.setter
    def coord(self, x, y):
        self._x = x
        self._y = y