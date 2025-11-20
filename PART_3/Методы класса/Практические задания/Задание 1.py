# Создайте класс `Car` с атрибутом `speed` (скорость). Используйте геттеры и сеттеры для:
#
# - Проверки, что скорость не может быть отрицательной
# - Проверки, что скорость не превышает 300 км/ч



class Car:
    def __init__(self, speed):
        self.speed_check(speed)
        self.__speed = speed


    @classmethod
    def speed_check(cls, speed):
        min_speed = 0
        max_speed = 300
        print(20 * '=' + 'ИЗМЕНЯЕМ СКОРОСТЬ!' + 20 * '=')
        print(f'Вы пытаетесь установить скорость равную {speed} км/ч')
        try:
            if min_speed < speed <= max_speed:
                cls.__speed = speed
                print(f'Успешно! Скорость установлена как {speed} км/ч.')
            else:
                raise ValueError()
        except ValueError:
            print(f'Ошибка! Скорость не может быть меньше чем {min_speed} км/ч или больше чем {max_speed} км/ч!')



    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.speed_check(speed)
        self.__speed = speed


car = Car(80)
car.speed = 150
car.speed = 200
car.speed = 50
car.speed = 1000
car.speed = -100
