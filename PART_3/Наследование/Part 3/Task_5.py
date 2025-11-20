class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} запускается обычным способом"

    def stop(self):
        return f"{self.brand} {self.model} останавливается"


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        # TODO: Инициализируй все атрибуты (пока дублируя код)
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    # TODO: Переопредели start(), чтобы учитывать fuel_type# Если fuel_type == "electric": "{brand} {model} запускается бесшумно на электричестве"
    # Иначе: "{brand} {model} запускается с рокотом двигателя на {fuel_type}"
    def start(self):
        if self.fuel_type == 'electric':
            return f'{self.brand} {self.model} запускается бесшумно на электричестве'
        else:
            return f'{self.brand} {self.model} запускается с рокотом двигателя на {self.fuel_type}'


class Motorcycle(Vehicle):
    # TODO: Переопредели start() для мотоцикла:# "{brand} {model} заводится с характерным звуком мотоцикла"
    def start(self):
        return f'{self.brand} {self.model} заводится с характерным звуком мотоцикла'


class Bicycle(Vehicle):
    # TODO: Переопредели start() для велосипеда:# "{brand} {model} готов к поездке - просто крути педали!"
    def start(self):
        return f'{self.brand} {self.model} готов к поездке - просто крути педали!'


# Тестирование:
vehicles = [
    Vehicle("Generic", "Transport"),
    Car("Tesla", "Model S", "electric"),
    Car("Toyota", "Camry", "бензин"),
    Motorcycle("Harley-Davidson", "Street 750"),
    Bicycle("Trek", "Mountain Bike")
]

print("=== Запуск транспорта ===")
for vehicle in vehicles:
    print(vehicle.start())

# Проверь, что stop() работает одинаково у всех (не переопределен)
print("\n=== Остановка транспорта ===")
for vehicle in vehicles:
    print(vehicle.stop())