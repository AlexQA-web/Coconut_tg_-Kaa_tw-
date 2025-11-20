# Напишите функцию `analyze_numbers(numbers)`, которая принимает **список** чисел и
# возвращает словарь со следующей информацией:
#
# - `"average"`: среднее значение чисел в списке.
# - `"min"`: минимальное число в списке.
# - `"max"`: максимальное число в списке.
# - `"even_count"`: количество четных чисел в списке
#
# Если список пустой, функция должна вернуть словарь со значениями `None` для всех ключей

def analyze_numbers(numbers):
    if not numbers:
        return print({'average': None ,
                      'min': None, 'max': None,
                      'even_count': None
                    })
    even_count = 0
    dict_from_list = {'average': sum(numbers) / len(numbers),
                      'min': min(numbers), 'max': max(numbers),
                      'even_count': even_count
                     }
    for i in numbers:
        if i % 2 == 0:
            even_count += 1
    return print(dict_from_list)


numbers = (1,3,2,4,6,5,7,9,8)
analyze_numbers(numbers)

# Perplexity

def analyze_numbers(numbers):
    if not numbers:
        return {
            "average": None,
            "min": None,
            "max": None,
            "even_count": None,
        }

    avg = sum(numbers) / len(numbers)
    mn = min(numbers)
    mx = max(numbers)
    even_count = sum(1 for x in numbers if isinstance(x, int) and x % 2 == 0)

    return {
        "average": avg,
        "min": mn,
        "max": mx,
        "even_count": even_count,
    }
