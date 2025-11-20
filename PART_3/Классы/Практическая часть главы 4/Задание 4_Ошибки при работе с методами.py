# В этом коде много ошибок! Найди и исправь их.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, subject):
        print(f"{self.name} изучает {subject}")

    def get_info(self):
        return f"Студент {self.name}, {self.grade} класс"

student = Student("Анна", 10)
# ToDo выполни код и исправь ошибки. После того как исправишь,
# раскомментировать следующие строки по одной и тоже исправь ошибки

print(student.study("математику"))

# print(Student.study("физику"))

# print(student.sleep())

# ToDo выполни код ниже и исправь ошибки
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

calc = Calculator(10, 5)

# раскомментировать следующие строки по одной и тоже исправь ошибки

result = calc.add(5, 3)
print(result)
result = calc.add(5, 2)
print(result)

print("Если ты видишь этот текст без ошибок - все исправлено правильно!")
