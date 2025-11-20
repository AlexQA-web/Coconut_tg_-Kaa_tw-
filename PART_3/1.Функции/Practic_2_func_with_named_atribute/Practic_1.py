# Написать функцию greet_person(name, age), которая принимает имя и возраст
# в качестве параметров.
# Функция должна выводить приветствие в формате: "Привет, [имя]! Тебе [возраст] лет."


def greet_person(name, age):
    print(f'Привет {name}! Тебе {age} лет.')


greet_person(age = 35, name = 'Alexey')
greet_person(name = 'Alexey', age = 35)
greet_person('Alexey', age = 35)
greet_person('Alexey', 35)
