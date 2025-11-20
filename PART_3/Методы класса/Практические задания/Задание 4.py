# Создайте класс `Rectangle` с атрибутами `width` и `height`. Добавьте следующие вычисляемые свойства:
#
# - `area` (площадь) - только для чтения
# - `perimeter` (периметр) - только для чтения
# - `diagonal` (диагональ) - только для чтения
#
# Также добавьте свойство `dimensions`, которое:
#
# - При чтении возвращает кортеж `(width, height)`
# - При записи принимает кортеж и устанавливает `width` и `height`
#
# **Требования:**
#
# - `width` и `height` должны быть положительными числами
# - При изменении размеров все вычисляемые свойства должны автоматически обновляться

class Rectangle:
    def __init__(self, width, height):
        self.side_check(width, height)
        self._width = width
        self._height = height



    @classmethod
    def side_check(cls, width, height):
        zero = 0
        if width <= zero or height <= zero:
            raise ValueError('Стороны должны быть больше ноля!')


    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._height + self._width)

    @property
    def diagonal(self):
        return (self._height ** 2 + self._width ** 2)**0.5

    @property
    def dimensions(self):
        return self._width, self._height

    @dimensions.setter
    def dimensions(self, tup):
        if not isinstance(tup, tuple) or len(tup) != 2:
            raise ValueError("Dimensions должен быть кортежем из двух элементов")
        width, height = tup
        self.side_check(width, height)
        self._width = width
        self._height = height




rect = Rectangle(5, 3)
print(rect.area)         # 15*
print(rect.perimeter)    # 16*
print(rect.diagonal)     # ~5.83*
print(rect.dimensions)   # (5, 3)*

rect.dimensions = (10, 6)
print(rect.area)         # 60*
print(rect.dimensions)   # (10, 6)*


