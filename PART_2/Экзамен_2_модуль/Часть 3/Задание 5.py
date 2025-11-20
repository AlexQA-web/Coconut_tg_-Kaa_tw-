# Создайте диапазон чисел от `1` до `20` включительно.
# Преобразуйте его в список.
# Найдите сумму всех чисел в списке.
# Найдите все числа, которые делятся на `3`, и создайте из них новый список.
# Выведите оба списка: оригинальный и новый.

start_range = range(1, 21)
new_list = list(start_range)
list_with_digit_on_3 = list()

for i in new_list:
    if i % 3 == 0:
        list_with_digit_on_3.append(i)
print(new_list)
print(list_with_digit_on_3)