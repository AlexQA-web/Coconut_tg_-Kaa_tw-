# Сделать переменную time, которая содержит время в секундах реализовать программу,
# которая переводит их в часы, минуты и секунды и выводит время на экран
# Пример работы:
# time = 3661
# результат работы: 1 час 1 минута 1 секунда


SEC_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

hours = 0
minutes = 0
seconds = 0
count = 0


time = int(input("Введите время в секундах: "))

for i in range(1,time + 1):
    count += 1
    if count % SEC_IN_MINUTE == 0:
        minutes += 1
        count = 0
        if minutes % MINUTES_IN_HOUR == 0:
            hours += 1
            minutes = 0
        else:
            pass
    else:
        seconds = count

print(f'Текущее время {hours}:{minutes}:{seconds}')
