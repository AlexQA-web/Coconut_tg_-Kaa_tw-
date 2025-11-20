class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # TODO: Создай метод area() - возвращает площадь (width * height)
    def area(self):
        return self.width * self.height

    # TODO: Создай метод perimeter() - возвращает периметр (2 * (width + height))
    def perimeter(self):
        return 2 * (self.width + self.height)

    # TODO: Создай метод is_square() - возвращает True если это квадрат
    def is_square(self):
        return True if self.width == self.height else False

    # TODO: Создай метод get_info() - возвращает словарь с информацией
    def get_info(self):
        # Верни словарь: {"width": self.width, "height": self.height, "area": площадь, "perimeter": периметр, "is_square": квадрат_или_нет}
        return {"width": self.width, "height": self.height, "area": self.area(), "perimeter": self.perimeter(), "is_square": self.is_square()}

    # TODO: Создай метод scale(factor) - увеличивает размеры в factor раз
    def scale(self, factor):
        # Умножь width и height на factor
        self.width *= factor
        self.height *= factor
        # Ничего не возвращай (метод изменяет объект)


    # TODO: Создай метод compare_area(other_rectangle) - сравнивает площади
    def compare_area(self, other_rectangle):
        my_area = self.area()
        other_area = other_rectangle.area()
        if my_area > other_area:
            return "больше"
        elif my_area < other_area:
            return "меньше"
        else:
            return "равна"
        # Верни строку: "больше", "меньше" или "равна"
        pass

# Тестирование:
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 7)  # Квадрат
rect3 = Rectangle(8, 6)

print("=== Информация о прямоугольниках ===")
print(f"Прямоугольник 1: {rect1.get_info()}")
print(f"Прямоугольник 2: {rect2.get_info()}")

print(f"\n=== Проверяем площади ===")
print(f"Площадь rect1: {rect1.area()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"Площадь rect1 {rect1.compare_area(rect2)} площади rect2")

print(f"\n=== Увеличиваем rect1 в 2 раза ===")
rect1.scale(2)
print(f"Новые размеры rect1: {rect1.width}x{rect1.height}")
print(f"Новая площадь: {rect1.area()}")
