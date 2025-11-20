# Создай родительский класс с несколькими методами и убедись, что дочерний класс их действительно наследует:

class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return f"Цвет: {self.color}"

    def describe(self):
        return "Это геометрическая фигура"


class Circle(Shape):
    pass

# Твой код для тестирования:
# 1. Создай объект Circle
ball = Circle('White')
# 2. Вызови все методы родительского класса
print(ball.get_color())
print(ball.describe())
# 3. Убедись, что они работают
