# Напишите программу, которая проверяет,
# входит ли заданное число в диапазон от 10 до 20 (включительно).

number = int(input('insert number: '))

if 10 <= number <= 20:
    print(f'{number} is between 10 and 20')
else:
    print(f'{number} is not between 10 and 20')