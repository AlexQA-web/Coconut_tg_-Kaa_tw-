# сделать переменную n. написать программу, которая выведет сумму всех чисел от 1 до n с помощью while

current = 1
summ = 0
end = int(input('Введите число: '))

while current <= end:
    summ += current
    current += 1
print(summ)

