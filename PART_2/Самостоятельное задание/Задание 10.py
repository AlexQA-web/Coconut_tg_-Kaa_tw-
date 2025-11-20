# сделать переменную n. написать программу, которая выведет сумму всех чисел от 1 до n

n = int(input('Введите число от 1 до 25: '))
main_list = list(range(1,n))
summ_a = 0

for i in main_list:
    summ_a += i
print(summ_a)