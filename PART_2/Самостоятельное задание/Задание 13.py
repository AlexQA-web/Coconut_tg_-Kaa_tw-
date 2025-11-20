# Поиск максимального элемента в списке
# Дано numbers = [3, 8, 1, 9, 4].
# Используя for, найти максимальное число


numbers = [3, 8, 1, 9, 4, 2, 7, 11, 22, 1, 17, 0]
max_number = 0

for i in numbers:
    if i > max_number:
        max_number = i
    else:
        continue
print(max_number)