# ### Задачи без return:
# 1. Создать функцию `print_even_numbers()`, которая выводит четные числа от 2 до 10
# 2. Создать функцию `print_countdown()`, которая выводит обратный отсчет от 5 до 1
# 3. Создать функцию `print_alphabet()`, которая выводит первые 5 букв алфавита
# 4. Создать функцию `print_multiplication_table()`, которая выводит таблицу умножения на 2 (от 1 до 5)
# 5. Создать функцию `print_triangle()`, которая выводит треугольник из звездочек (1, 2, 3, 4, 5 звездочек в строках)

def print_even_numbers():
    for i in range(2,10):
        if i % 2 == 0:
            print(i)

print_even_numbers()
print('######################################################################')

def print_countdown():
    for i in range(5, 0,-1):
        print(i)

print_countdown()
print('######################################################################')

def print_alphabet():
    alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    print(alphabet[0:5])

print_alphabet()
print('######################################################################')

def print_multiplication_table():
    num = 2
    for i in range(1, 6):
        print(i * num)

print_multiplication_table()
print('######################################################################')

def print_triangle():
    for i in range(1,6):
        print(i * '*')

print_triangle()
print('######################################################################')

### Задачи с return:

# 1. Создать функцию `sum_first_ten()`, которая возвращает сумму чисел от 1 до 10
def sum_first_ten():
    return sum(range(1,11))

print(f'сумма чисел от 1 до 10 равна {sum_first_ten()}')
print('######################################################################')

# 2. Создать функцию `count_vowels_in_hello()`, которая возвращает количество гласных в слове "hello"
def count_vowels_in_hello():
    vowels = 'AEIOUaeiou'
    phrase = 'Hello'
    count = 0
    for word in phrase:
        if word in vowels:
            count += 1
    return count

print(f'количество гласных в слове "hello" {count_vowels_in_hello()}')
print('######################################################################')

# 3. Создать функцию `get_max_from_list()`, которая возвращает максимальное число из списка [1, 5, 3, 9, 2]
def get_max_from_list():
    return max([1, 5, 3, 9, 2])

print(f'максимальное число из списка [1, 5, 3, 9, 2] = {get_max_from_list()}')
print('######################################################################')

# 4. Создать функцию `calculate_area_of_square()`, которая возвращает площадь квадрата со стороной 4
def calculate_area_of_square():
    return 4 ** 2

print(f'площадь квадрата со стороной 4 = {calculate_area_of_square()}')
print('######################################################################')

# 5. Создать функцию `get_length_of_alphabet()`, которая возвращает количество букв в алфавите (26)
def get_length_of_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return len(alphabet)

print(f'количество букв в алфавите = {get_length_of_alphabet()}')
