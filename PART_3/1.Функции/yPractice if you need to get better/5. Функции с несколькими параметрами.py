print('# 1. Создать функцию `greet_person(first_name, last_name)`, которая выводит полное приветствие')
def greet_person(first_name, last_name):
    print(f'Hello {first_name} {last_name}!')

greet_person('Python', 'Pytonovich')
print('----------------------------------------------------------------------------------')

print('# 2. Создать функцию `compare_numbers(a, b)`, которая выводит, какое число больше')
def compare_numbers(a, b):
    print(max(a, b))

compare_numbers(1, 2)
print('----------------------------------------------------------------------------------')

print('# 3. Создать функцию `print_info(name, age, city)`, которая выводит информацию о человеке')
def print_info(name, age, city):
    print(f'Имя: {name}, Возраст: {age}, Город: {city}')

print_info('Alexey', 21, 'N-sk')
print('----------------------------------------------------------------------------------')

print('# 4. Создать функцию `add_numbers(a, b)`, которая возвращает сумму двух чисел')
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))
print('----------------------------------------------------------------------------------')

print('# 5. Создать функцию `get_full_name(first, last)`, которая возвращает полное имя')
def get_full_name(first, last):
    return first + ' ' + last

print(get_full_name('Python', 'Pytonov'))
print('----------------------------------------------------------------------------------')

print('# 6. Создать функцию `calculate_area(length, width)`, которая возвращает площадь прямоугольника')
def calculate_area(length, width):
    return length * width

print(calculate_area(2,5))
print('----------------------------------------------------------------------------------')

print('# 7. Создать функцию `find_max(a, b, c)`, которая возвращает максимальное из трех чисел')
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(5,7,1))
print('----------------------------------------------------------------------------------')