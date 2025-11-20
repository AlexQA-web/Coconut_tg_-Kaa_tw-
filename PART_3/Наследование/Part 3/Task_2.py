class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Человек: {self.name}, {self.age} лет"


class Student(Person):
    def __init__(self, name, age, university):
        # TODO: Инициализируй атрибуты (пока дублируя код)
        self.name = name
        self.age = age
        self.university = university

    # TODO: Переопредели __str__(), чтобы возвращал
    # "Студент: {name}, {age} лет, учится в {university}"
    def __str__(self):
        return f"Студент: {self.name}, {self.age} лет, учится в {self.university}"


class Employee(Person):
    def __init__(self, name, age, company):
        # TODO: Инициализируй атрибуты (пока дублируя код)
        self.name = name
        self.age = age
        self.company = company

    # TODO: Переопредели __str__(), чтобы возвращал# "Сотрудник: {name}, {age} лет, работает в {company}"
    def __str__(self):
        return f"Сотрудник: {self.name}, {self.age} лет, работает в {self.company}"


# Тестирование:
people = [
    Person("Алексей", 30),
    Student("Мария", 20, "МГУ"),
    Employee("Петр", 35, "Google")
]

for person in people:
    print(person)  # Вызовется переопределенный __str__
    # Ожидаемый результат:
    # Человек: Алексей, 30 лет
    # Студент: Мария, 20 лет, учится в МГУ
    # Сотрудник: Петр, 35 лет, работает в Google