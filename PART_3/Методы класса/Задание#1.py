# **Реестр животных**
# Создай класс `Animal` с атрибутом класса `species` (список всех зарегистрированных видов животных)
# Реализуй метод класса `add_species`, который добавляет новый вид в реестр при создании объекта,
# и метод `show_species`, который выводит список всех видов
# При этом, если уже в реестре есть такой тип животного, то `add_species` не должен его добавлять в этот реестр.

class Animal:
    species = []
    def __init__(self, animal_type):
        self.animal_type = animal_type
        self.add_species(animal_type)

    @classmethod
    def add_species(cls, type):
        if type not in cls.species:
            cls.species.append(type)

    @classmethod
    def show_species(cls):
        print(cls.species)


animal1 = Animal('Cat')
animal2 = Animal('Dog')
animal3 = Animal('Bird')
animal4 = Animal('Cat')

Animal.show_species()