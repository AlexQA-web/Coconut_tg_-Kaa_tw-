# - Задание 1: \
# (Исправление) дублирования в конструкторах
# ** Цель: ** заменить дублирование кода на super()

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.vehicle_id = f"{brand}_{model}_{year}"
        print(f"Создан транспорт: {brand} {model} {year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.vehicle_id = f"{brand}_{model}_{year}"
        print(f"Создан транспорт: {brand} {model} {year}")

        self.doors = doors
        print(f"Добавлено {doors} дверей")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.vehicle_id = f"{brand}_{model}_{year}"
        print(f"Создан транспорт: {brand} {model} {year}")

        self.engine_volume = engine_volume
        print(f"Объем двигателя: {engine_volume}л")


# TODO: Перепиши Car и Motorcycle, используя super().__init__()
# Убедись, что результат работы остался точно таким же!
# Тестирование:
car = Car("Toyota", "Camry", 2022, 4)
moto = Motorcycle("Yamaha", "R1", 2023, 1.0)

print(f"Car ID: {car.vehicle_id}")
print(f"Moto ID: {moto.vehicle_id}")