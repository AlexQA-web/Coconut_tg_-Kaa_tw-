print('1. Создать функцию `double(x)`, которая возвращает x*2, и функцию `print_double_result(num)`,\n которая выводит результат функции double')
def double(x):
    return x * 2

def print_double_result(num):
    print(double(num))

print_double_result(7)
print('-----------------------------------------------------------------------------------------')

print('2. Создать функцию `get_square(x)`, которая возвращает x², и функцию `sum_of_squares(a, b)`,\n которая возвращает сумму квадратов двух чисел (для вычисления квадрата числа использовать первую функцию)')
def get_square(x):
    return x ** 2

def sum_of_squares(a, b):
    return get_square(a) + get_square(b)

print(sum_of_squares(2, 3))
print('-----------------------------------------------------------------------------------------')

print('3. Создать функцию `get_length(text)` и функцию `compare_lengths(text1, text2)`,\n которая сравнивает длины строк')
def get_length(text):
    return len(text)

def compare_lengths(text1, text2):
    if get_length(text1) > get_length(text2):
        return 'Text 1 is bigger'
    elif get_length(text2) > get_length(text1):
        return 'Text 2 is bigger'
    else:
        return 'Texts is same'

print(compare_lengths('Asdfresv', 'dffjierjejeeg'))
print('-----------------------------------------------------------------------------------------')

print('4. Создать функцию `celsius_to_fahrenheit(c)` которая переводит цельсия в фаренгейты\n и функцию `compare_temperatures(c1, c2)`, которая сравнивает температуры в Фаренгейтах')
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def compare_temperatures(c1, c2):
    if celsius_to_fahrenheit(c1) > celsius_to_fahrenheit(c2):
        return f'Temperature {c1} celsius is bigger then {c2} in Fahrengeit'
    elif celsius_to_fahrenheit(c2) > celsius_to_fahrenheit(c1):
        return f'Temperature {c2} celsius is bigger then {c1} in Fahrengeit'
    else:
        return 'Temperature is same'

print(compare_temperatures(23, 32))

print('-----------------------------------------------------------------------------------------')
print('5. Создать функцию `add_ten(x)` и функцию `process_numbers(a, b)`, которая к каждому числу\n добавляет 10 и возвращает их сумму')
def add_ten(x):
    return x + 10

def process_numbers(a, b):
    return add_ten(a) + add_ten(b)

print(process_numbers(2, 5))
print('-----------------------------------------------------------------------------------------')

print('6. Создать функцию `multiply_by_two(x)` и функцию `calculate_perimeter(length, width)`, которая\n вычисляет периметр, используя удвоение')
def multiply_by_two(x):
    return x * 2

def calculate_perimeter(length, width):
    return multiply_by_two(length) + multiply_by_two(width)

print(calculate_perimeter(5, 7))
print('-----------------------------------------------------------------------------------------')

print('7. Создать функцию `is_even(x)` и функцию `filter_even_sum(a, b, c)`, которая суммирует только\n четные числа из трех переданных')
def is_even(x):
    return x // 2 == 0

def filter_even_sum(a, b, c):
    return sum(i for i in (a, b, c) if i % 2 == 0)

print(filter_even_sum(1, 4, 5))
print('-----------------------------------------------------------------------------------------')