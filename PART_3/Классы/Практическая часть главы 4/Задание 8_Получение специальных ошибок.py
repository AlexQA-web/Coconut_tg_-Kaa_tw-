class TestClass:
    def __init__(self, value):
        self.value = value

    def method_with_self(self):
        return f"Значение: {self.value}"

    def method_with_params(self, a, b):
        return a + b

obj = TestClass(42)

print("=== Эксперимент 1: Вызов метода через класс ===")
# TODO: Попробуй вызвать метод через класс напрямую
result = TestClass.method_with_self(obj)  # Раскомментируй и посмотри ошибку
print(result)

print("=== Эксперимент 2: Передача self вручную ===")
# TODO: Попробуй передать self вручную
result = TestClass.method_with_self(obj)  # Это работает!
print(f"Результат: {result}")

print("=== Эксперимент 3: Неправильное количество параметров ===")
# TODO: Попробуй разные варианты (раскомментируй по одному):
# result = obj.method_with_params()        # Мало параметров
# result = obj.method_with_params(1)       # Мало параметров
# result = obj.method_with_params(1, 2, 3) # Много параметров

print("=== Эксперимент 4: Вызов несуществующего метода ===")
# TODO: Попробуй вызвать несуществующий метод
# result = obj.nonexistent_method()  # Раскомментируй и посмотри ошибку

print("=== Эксперимент 5: Обращение к несуществующему атрибуту в методе ===")
class BuggyClass:
    def __init__(self):
        self.existing_attr = "существует"

    def buggy_method(self):
        return self.nonexistent_attr  # Ошибка!

buggy_obj = BuggyClass()
# TODO: Попробуй вызвать метод с ошибкой
# result = buggy_obj.buggy_method()  # Раскомментируй и посмотри ошибку

# TODO: После каждого эксперимента запиши:
# 1. Какая ошибка возникла?
# 2. Что означает текст ошибки?
# 3. Как исправить эту ошибку?

print("Эксперименты завершены!")
