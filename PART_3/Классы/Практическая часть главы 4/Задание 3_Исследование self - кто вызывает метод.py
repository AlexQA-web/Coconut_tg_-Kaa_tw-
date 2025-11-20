class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет")
        print(f"ID объекта в методе introduce: {id(self)}")
        return f"Я {self.name}"

    def have_birthday(self):
        print(f"{self.name} празднует день рождения!")
        self.age += 1
        print(f"Теперь {self.name} {self.age} лет")
        print(f"ID объекта в методе have_birthday: {id(self)}")

# TODO: Создай трех людей
person1 = Person("Анна", 25)
person2 = Person("Петр", 30)
person3 = Person("Мария", 22)

print("=== Знакомство ===")
person1.introduce()
person2.introduce()
person3.introduce()

print(f"\n=== ID объектов снаружи ===")
print(f"person1 ID: {id(person1)}")
print(f"person2 ID: {id(person2)}")
print(f"person3 ID: {id(person3)}")

print(f"\n=== Дни рождения ===")
person1.have_birthday()  # У Анны день рождения
person3.have_birthday()  # У Марии день рождения

print(f"\n=== Проверяем возрасты ===")
print(f"Анна: {person1.age} лет")
print(f"Петр: {person2.age} лет")  # Не изменился!
print(f"Мария: {person3.age} лет")

# Вопросы для селфчека:
# 1. Совпадают ли ID в методах с ID объектов снаружи?
# 2. Почему возраст Петра не изменился?
# 3. Как Python понимает, у какого объекта вызвать метод?
