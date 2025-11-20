# - Задание
# 4: Цепочка валидации
# ** Цель: ** Создать цепочку обработки с super()



class BaseValidator:
    def __init__(self, name):
        self.name = name
        self.errors = []

    def validate(self, data):
        print(f"[{self.name}] Начинаем валидацию: {data}")
        self.errors.clear()
        return True


class LengthValidator(BaseValidator):
    def __init__(self, name, min_length):
        super().__init__(name)
        self.min_length = min_length

    def validate(self, data):
        # TODO: Вызови родительский метод validate
        super().validate(data)
        # TODO: Добавь проверку длины*
        if len(str(data)) < self.min_length:
            self.errors.append(f"Слишком короткое значение (минимум {self.min_length})")
            return False
        return True


class FormatValidator(LengthValidator):
    def __init__(self, name, min_length, required_symbol):
        # TODO: Инициализируй родительский класс*
        super().__init__(name, min_length)
        self.required_symbol = required_symbol

    def validate(self, data):
        # TODO: Вызови родительский метод (включает базовую и длину)*
        if not super().validate(data):
            return False

        # TODO: Добавь проверку формата*
        if self.required_symbol not in str(data):
            self.errors.append(f"Отсутствует обязательный символ '{self.required_symbol}'")
            return False
        return True

# Тестирование:*
validator = FormatValidator("EmailValidator", 5, "@")

# Тест 1: Все проверки пройдены*
print("=== Тест 1 ===")
result1 = validator.validate("user@example.com")
print(f"Результат: {result1}")
print(f"Ошибки: {validator.errors}")

# Тест 2: Слишком короткое
print("\n=== Тест 2 ===")
result2 = validator.validate("abc")
print(f"Результат: {result2}")
print(f"Ошибки: {validator.errors}")

 # Тест 3: Нет @ символа*
print("\n=== Тест 3 ===")
result3 = validator.validate("verylongemail.com")
print(f"Результат: {result3}")
print(f"Ошибки: {validator.errors}")
