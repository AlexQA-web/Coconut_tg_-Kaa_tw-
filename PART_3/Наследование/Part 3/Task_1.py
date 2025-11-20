class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} издает звук"


class Dog(Animal):
    # TODO: Переопредели make_sound(), чтобы возвращал "{name} лает: Гав-гав!"
    def make_sound(self):
        return f"{self.name} лает: Гав-гав!"


class Cat(Animal):
    # TODO: Переопредели make_sound(), чтобы возвращал "{name} мяукает: Мяу!"
    def make_sound(self):
        return f"{self.name} мяукает: Мяу!"


class Cow(Animal):
    # TODO: Переопредели make_sound(), чтобы возвращал "{name} мычит: Му-у!"
    def make_sound(self):
        return f"{self.name} мычит: Му-у!"


# Тестирование:
animals = [
    Animal("Неизвестное животное"),
    Dog("Рекс"),
    Cat("Мурка"),
    Cow("Буренка")
]

for animal in animals:
    print(animal.make_sound())

# Ожидаемый результат:
# Неизвестное животное издает звук
# Рекс лает: Гав-гав!#
# Мурка мяукает: Мяу!
# Буренка мычит: Му-у!