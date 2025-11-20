print('# 1. Создать функцию `outer_function()`, внутри которой есть функция `inner_function()`,\n которая выводит "Внутренняя функция"')
def outer_function():
    def inner_function():
        print('Внутренняя функция')
    inner_function()

outer_function()
print('-------------------------------------------------------------------------------------------------')

print('# 2. Создать функцию `number_analyzer(num)`, внутри которой есть функции `is_positive()` и\n `is_even()`, возвращающую полный анализ числа')
def number_analyzer(num):
    # вложенная функция: положительное ли число
    def is_positive():
        return num > 0

    # вложенная функция: чётное ли число (осмысленно для целых; для float учитываем только целочисленные)
    def is_even():
        if isinstance(num, bool):
            return False  # исключаем булевы, хотя они подкласс int
        if isinstance(num, int):
            return num % 2 == 0
        if isinstance(num, float) and num.is_integer():
            return int(num) % 2 == 0
        return None  # не применимо для нецелых значений

    return {
        "value": num,
        "is_positive": is_positive(),
        "is_even": is_even(),
        "sign": "positive" if num > 0 else "negative" if num < 0 else "zero",
    }

print(number_analyzer(21))