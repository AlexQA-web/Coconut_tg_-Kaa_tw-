# Напишите программу, которая:
# Сравнивает сумму двух чисел с третьим числом.
# Проверяет, меньше ли произведение двух чисел, чем третье число.

a = int(input('insert A: '))
b = int(input('insert B: '))
c = int(input('insert C: '))

if (a + b) > c:
    print(f'SUM {a} and {b} bigger then {c}')
elif (a + b) < c:
    print(f'SUM {a} and {b} smaller then {c}')
else:
    print(f'SUM {a} and {b} is equal to {c}')
assert a * b < c,  f"{a} * {b} is not smaller then {c}"




