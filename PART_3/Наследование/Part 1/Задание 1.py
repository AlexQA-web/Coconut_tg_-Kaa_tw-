# Создай пустой класс Vehicle и класс Car, который наследует от Vehicle.
# Создай объект класса Car и выведите список его атрибутов с помощью dir()
# Убедись, что Car автоматически получил методы от object
#

class Vehicle:
    def get_colour(self):
        return self.colour


class Car(Vehicle):
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour

car_1 = Car('Toyota', 'Highlander', 'White')
print(car_1.get_colour())
print(dir(car_1))


