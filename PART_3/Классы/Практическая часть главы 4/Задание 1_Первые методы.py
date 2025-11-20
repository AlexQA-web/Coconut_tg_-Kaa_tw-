# TODO: Создай класс Calculator с методами:
# add(a, b) - сложение
# subtract(a, b) - вычитание
# multiply(a, b) - умножение
# divide(a, b) - деление

class Calculator:
    def add(self, a, b):
        # TODO: верни результат сложения a + b
        return a + b

    def subtract(self, a, b):
        # TODO: верни результат вычитания a - b
        return a - b

    def multiply(self, a, b):
        # TODO: верни результат умножения a * b
        return a * b

    def divide(self, a, b):
        # TODO: верни результат деления a / b
        # Добавь проверку деления на ноль
        try:
            return a / b
        except ZeroDivisionError:
            print('Деление на ноль запрещено!')


# TODO: Создай объект калькулятора и протестируй все методы
calc = Calculator()

print(f"10 + 5 = {calc.add(10, 5)}")           # Должно быть 15
print(f"10 - 5 = {calc.subtract(10, 5)}")     # Должно быть 5
print(f"10 * 5 = {calc.multiply(10, 5)}")     # Должно быть 50
print(f"10 / 5 = {calc.divide(10, 5)}")       # Должно быть 2.0
print(f"10 / 0 = {calc.divide(10, 0)}")       # Должно обработать ошибку
