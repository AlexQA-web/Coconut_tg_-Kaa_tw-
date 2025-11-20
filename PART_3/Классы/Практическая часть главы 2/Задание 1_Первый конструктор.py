# TODO: Создай класс Car с конструктором, который принимает:
# brand (марка), model (модель), year (год)
# В конструкторе устанавливай эти атрибуты через self
# Добавь атрибут mileage = 0 (пробег по умолчанию)

class Car:
    def __init__(self, brand, model, year):
        self.brand  = brand
        self.model = model
        self.year = year
        self.mileage = 0
    pass

# TODO: Создай три машины:
car1 = Car('Toyota', 'Camry', '2020')  # "Toyota", "Camry", 2020
car2 = Car('BMW', 'X5', '2022')  # "BMW", "X5", 2022
car3 = Car('Lada', 'Granta', '2019')  # "Lada", "Granta", 2019# Проверь результат:
print(f"Машина 1: {car1.brand} {car1.model} ({car1.year}), пробег: {car1.mileage} км")
print(f"Машина 2: {car2.brand} {car2.model} ({car2.year}), пробег: {car2.mileage} км")
print(f"Машина 3: {car3.brand} {car3.model} ({car3.year}), пробег: {car3.mileage} км")

# Ожидаемый результат:
# Машина 1: Toyota Camry (2020), пробег: 0 км
# Машина 2: BMW X5 (2022), пробег: 0 км
# Машина 3: Lada Granta (2019), пробег: 0 км