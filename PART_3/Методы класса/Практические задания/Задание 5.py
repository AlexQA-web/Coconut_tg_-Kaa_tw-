# Создайте класс `Counter` со следующими возможностями:
#
# - Свойство `value` - текущее значение счетчика
# - Свойство `history` - список всех значений (только для чтения)
# - Свойство `change_count` - количество изменений (только для чтения)
#
# **Особенности:**
#
# - При каждом изменении `value` старое значение сохраняется в историю
# - Начальное значение тоже должно быть в истории
# - Нельзя устанавливать одно и то же значение подряд

class Counter:
    def __init__(self, value):
        self._change_count = 0
        self._value = value
        self._history = [value]


    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value != self._value:
            self._change_count += 1
            self._history.append(value)
            self._value = value

    @property
    def history(self):
        return self._history

    @property
    def change_count(self):
        return self._change_count


counter = Counter(10)
print(counter.value)        # 10
print(counter.history)      # [10]
print(counter.change_count) # 0

counter.value = 15
counter.value = 15          # Не должно изменить историю
counter.value = 20

print(counter.history)      # [10, 15, 20]
print(counter.change_count) # 2

