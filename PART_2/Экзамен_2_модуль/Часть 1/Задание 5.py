#Напишите программу, которая:
#Выполняет одну из арифметических операций (`+`, , , `/`, `%`, `//`, `*`) между двумя числами.
#Если операция деления (`/`, `//`, `%`) выбирается при втором числе равном 0, программа должна выводить сообщение об ошибке.

a = int(input('Enter a number: '))
c = input('Enter an action: ')
b = int(input('Enter another number: '))

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print("You can't divide by zero")
elif c == '%':
    if b != 0:
        print(a % b)
    else:
        print("You can't divide by zero")
elif c == '**':
    print(a ** b)
elif c == '//':
    if b != 0:
        print(a // b)
    else:
        print("You can't divide by zero")
else:
    print('Invalid input')