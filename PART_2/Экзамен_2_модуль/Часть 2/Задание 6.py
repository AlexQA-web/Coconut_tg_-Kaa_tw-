# **Обработка строки и числа вместе**
# Напишите программу, которая:
# Создаёт строку `data = "Price: 1234.5678 USD"`.
# Извлекает числовую часть строки (1234.5678) с помощью среза и преобразует её в число.
# Округляет это число до двух знаков после запятой.
# Формирует новую строку вида: `"Rounded price: 1234.57 USD"` и выводит её.
from operator import index

data = 'Price: 1234.5678 USD'
index_1 = data.index('1')
index_2 = data.index('8')
price = round(float(data[index_1:(index_2 + 1)]), 2)

print(f'Rounded price: {price} USD')
