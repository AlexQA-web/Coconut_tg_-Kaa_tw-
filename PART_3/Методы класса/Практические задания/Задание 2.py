# Вот код, который не работает. Найдите все ошибки и исправьте их:

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        print(f"Текущая температура: {self._celsius}°C")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Слишком холодно!")
        self._celsius = value


    def fahrenheit(self, value):
        celsius_value = (value - 32) * 5 / 9
        self._celsius = celsius_value


# Попробуйте запустить этот код:
temp = Temperature(25)
print(temp.celsius)
temp.celsius = 30
print(temp.celsius)
temp.fahrenheit(86)
print(temp.celsius)
