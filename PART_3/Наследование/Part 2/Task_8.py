class Animal:
    species_count = 0  # Атрибут класса

    def __init__(self, name):
        self.name = name  # Атрибут экземпляра
        Animal.species_count += 1


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# Пробуем:
dog1 = Dog("Бобик")
cat1 = Cat("Мурка")
dog2 = Dog("Шарик")

# Исследуй:
# 1. Что показывает Animal.species_count?  3
print(Animal.species_count)
# 2. Что показывает Dog.species_count?   3
print(Dog.species_count)
# 3. Что показывает Cat.species_count?   3
print(Cat.species_count)
# 4. Что показывает dog1.__dict__?   {'name': 'Бобик'}
print(dog1.__dict__)
# 5. Что показывает Dog.__dict__?     {'__module__': '__main__', '__firstlineno__': 9, '__static_attributes__': (), '__doc__': None}
print(Dog.__dict__)
# Попробуй изменить Dog.species_count = 100
Dog.species_count = 100
# Как это повлияет на Animal.species_count и Cat.species_count? Никак
