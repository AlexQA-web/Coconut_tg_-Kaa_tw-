# Задачи без return:
# 1. Создать функцию `say_hello()`, которая выводит "Привет!"
# 2. Создать функцию `print_stars()`, которая выводит 5 звездочек: *****
# 3. Создать функцию `print_line()`, которая выводит горизонтальную линию из 20 дефисов
# 4. Создать функцию `goodbye()`, которая выводит "До свидания!"

# 1
def print_line():
    print(20 * '-')

print_line()

def say_hello():
    print('Привет!')

say_hello()

def print_stars():
    print(5 * '*')

print_stars()

def goodbye():
    print('До свидания!')

goodbye()
print_line()

# 1. Создать функцию `get_my_name()`, которая возвращает ваше имя
# Результат работы функции (то что она вернет), положить в переменную
# Вывести при помощи print содержимое этой переменной

# 2. Создать функцию `get_lucky_number()`, которая возвращает число 7
# Напечатать результат отдельно от функции

# 3. Создать функцию `get_greeting()`, которая возвращает строку "Добро пожаловать!"
# Напечатать результат отдельно от функции

def get_my_name():
    return 'Alexey'

my_name = get_my_name()
print(my_name)

#######################################################
number = 0

def get_lucky_number():
    global number
    number = 7
    return number

get_lucky_number()
print(number)
########################################################

string = ''

def get_greeting():
    global string
    string = 'Добро пожаловать!'
    return string

get_greeting()
print(string)