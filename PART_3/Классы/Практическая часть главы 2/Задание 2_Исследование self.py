class Person:
    def __init__(self, name, age):
        print(f"Создается человек: {name}")
        print(f"ID объекта в self: {id(self)}")

        self.name = name
        self.age = age

        print(f"Установлено: self.name = {self.name}")
        print(f"Возраст записан для объекта {id(self)}: {self.age}")
        print("-" * 50)

# TODO: Создай трех людей
persona_1 = Person('Alex', 25)
persona_2 = Person('Nata', 35)
persona_3 = Person('Ivan', 5)

# TODO: Проверь ID объектов снаружи и сравни с выводом конструктора

print(id(persona_1), id(persona_2), id(persona_3))

# TODO: Убедись что каждый объект имеет свои атрибуты (используя print())

print(persona_3.__dict__, persona_2.__dict__, persona_1.__dict__)

# Вопросы для самостоятельного исследования:
# 1. Совпадают ли ID в конструкторе с ID объектов снаружи?  ДА, СОВПАДАЮТ
