# Написать функцию для деления двух чисел с обработкой исключений.

def safe_divide(a, b):
    try:
        a / b
    except ZeroDivisionError:
        return 'Ошибка! На ноль делить нельзя'
    except Exception:
        return 'Ошибка! Введите целое число'
    else:
        return a / b

print(safe_divide(2, 'c'))