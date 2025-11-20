# Создай классы и намеренно передай неправильное количество аргументов, чтобы посмотреть на ошибки:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    pass

# Попробуй создать объекты с неправильным количеством аргументов:
st_1 = Student('Alexey')

# 1. Создай Person только с одним аргументом
#teacher_1 = Person('Oleg')

# 2. Создай Student без аргументов
#st_2 = Student()

# 3. Создай Student с тремя аргументами
# st_3 = Student('Alex', 23, 45)
# Внимательно посмотри, в каком классе Python показывает ошибку в каждом случае