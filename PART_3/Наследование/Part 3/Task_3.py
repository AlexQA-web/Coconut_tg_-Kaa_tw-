import math


class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0  # Базовая реализация

    def describe(self):
        return f"{self.color} фигура с площадью {self.area()}"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        # TODO: Инициализируй все атрибуты (пока дублируя self.color)
        self.color = color
        self.width = width
        self.height = height

    # TODO: Переопредели area() для расчета площади прямоугольника
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        # TODO: Инициализируй все атрибуты (пока дублируя self.color)
        self.color = color
        self.radius = radius

    # TODO: Переопредели area() для расчета площади круга (используй math.pi)
    def area(self):
        return math.pi * self.radius * 2


class Triangle(Shape):
    def __init__(self, color, base, height):
        # TODO: Инициализируй все атрибуты
        self.color = color
        self.base = base
        self.height = height

    # TODO: Переопредели area() для расчета площади треугольника (base * height / 2)
    def area(self):
        return self.base * self.height / 2


# Тестирование полиморфизма:
shapes = [
    Shape("серая"),
    Rectangle("красный", 5, 3),
    Circle("синий", 2),
    Triangle("зеленый", 4, 6)
]

for shape in shapes:
    print(shape.describe())

# Ожидаемый результат (примерно):
# серая фигура с площадью 0
# красный фигура с площадью 15
# синий фигура с площадью 12.566370614359172
# зеленый фигура с площадью 12.0
