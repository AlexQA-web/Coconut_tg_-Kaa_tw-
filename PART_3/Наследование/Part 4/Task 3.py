# - Задание
# 3: Исследование передачи параметров
# Передаем параметры через super()


class Calculator:
    def __init__(self, name):
        self.name = name
        self.operations_count = 0

    def calculate(self, operation, a, b, precision=2):
        self.operations_count += 1
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        else:
            result = 0

        return round(result, precision)


class AdvancedCalculator(Calculator):
    def __init__(self, name, max_precision):
        super().__init__(name)
        self.max_precision = max_precision

    def calculate(self, operation, a, b, precision=2):
        precision = min(precision, self.max_precision)
        # TODO: Вызови родительский метод с ПРАВИЛЬНЫМИ параметрами# НЕ передавай self! Передай operation, a, b, precision*
        result = super().calculate(operation, a, b, precision)
        print(f"[{self.name}] {operation}({a}, {b}) = {result}")
        return result


class ScientificCalculator(AdvancedCalculator):
    def calculate(self, operation, a, b, precision=2):
        try:
            result = super().calculate(operation, a, b, precision)
            return result
        except:
             # Обрабатываем дополнительные операции*
            if operation == "power":
                result = round(a ** b, precision)
                print(f"[{self.name}] power({a}, {b}) = {result}")
                return result
            return 0

# Тестирование:*
calc = ScientificCalculator("Sci-Calc", 3)
print("Результат 1:", calc.calculate("add", 10.12345, 5.67890, 4))   # precision ограничится до 3*
print("Результат 2:", calc.calculate("power", 2, 8, 1))   # новая операция*
print("Результат 3:", calc.calculate("subtract", 100, 25.5555, 2))  # обычная операция*

print(f"Операций выполнено: {calc.operations_count}")
