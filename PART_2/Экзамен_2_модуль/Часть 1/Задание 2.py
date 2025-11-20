# Напишите программу, которая сравнивает два числа и выводит:
# Число `a` больше, меньше или равно числу `b`.

a = int(input('insert A: '))
b = int(input('insert B: '))

if a > b:
    print('A bigger then B')
elif a < b:
    print('A smaller then B')
else:
    print('A is equal to B')