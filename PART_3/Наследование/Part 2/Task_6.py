class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    pass  # Не добавляем свой __init__

class Teacher(Person):
    def __init__(self, name, age, subject):  # Добавляем свой __init__
        self.name = name
        self.age = age
        self.subject = subject

# Попробуй создать объекты разными способами и получи ошибки:
           # 1. Student("Иван") -- 1 параметр вместо 2
# student_1 = Student("Иван")   # TypeError: Person.__init__() missing 1 required positional argument: 'age'
           # 2. Student("Мария", 20, "Математика") -- 3 параметра вместо 2
#student_2 = Student("Мария", 20, "Математика")     # TypeError: Person.__init__() takes 3 positional arguments but 4 were given
           # 3. Teacher("Петр", 35) -- 2 параметра вместо 3
#teacher_1 = Teacher("Петр", 35)  # TypeError: Teacher.__init__() missing 1 required positional argument: 'subject'
           # 4. Teacher("Анна") -- 1 параметр вместо 3# Для каждого случая:
teacher_2 = Teacher("Анна")   # TypeError: Teacher.__init__() missing 2 required positional arguments: 'age' and 'subject'
# - Запиши текст ошибки
# - Определи, в каком классе Python ищет __init__ 1 & 2 Person.__init__() 3 & 4 Teacher.__init__()
# - Возникшие ошибки уже должны быть очевидны и заранее предвидены