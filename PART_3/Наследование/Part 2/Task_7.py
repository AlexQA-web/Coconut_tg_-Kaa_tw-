class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"{self.brand} движется"


class LandVehicle(Vehicle):
    def drive_on_road(self):
        return f"{self.brand} едет по дороге"


class Car(LandVehicle):
    def park(self):
        return f"{self.brand} паркуется"


class Truck(LandVehicle):
    def load_cargo(self):
        return f"{self.brand} загружает груз"


# Создай объекты Car и Truck# Проверь, какие методы доступны каждому:
car = Car("Toyota")
truck = Truck("Volvo")

# Протестируй для каждого объекта:
# 1. Методы от Vehicle
print(car.move())
print(truck.move())
# 2. Методы от LandVehicle
print(car.drive_on_road())
print(truck.drive_on_road())
# 3. Собственные методы
print(car.park())
print(truck.load_cargo())
# 4. Попробуй вызвать car.load_cargo() - что получится?    # AttributeError: 'Car' object has no attribute 'load_cargo'
