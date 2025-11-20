class Vehicle:
    #TODO: Реализуйте конструктор с параметрами brand, model, year# TODO: Добавьте метод start_engine(), который возвращает строку "{brand} {model} заводится"
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f'{self.brand} {self.model} заводится'

class Car(Vehicle):
    # TODO: Добавьте метод honk(), который возвращает "{brand} {model} сигналит: Би-бип!"
    def honk(self):
        return f'{self.brand} {self.model} сигналит: Би-бип!'

class Motorcycle(Vehicle):
    # TODO: Добавьте метод wheelie(), который возвращает "{brand} {model} делает вилли!"
    def wheelie(self):
        return f'{self.brand} {self.model} делает вилли!'

# Тестирование:
car = Car("Toyota", "Camry", 2022)
print(car.start_engine())  # Toyota Camry заводится
print(car.honk())          # Toyota Camry сигналит: Би-бип!

moto = Motorcycle("Yamaha", "R1", 2023)
print(moto.start_engine()) # Yamaha R1 заводится
print(moto.wheelie())      # Yamaha R1 делает вилли!