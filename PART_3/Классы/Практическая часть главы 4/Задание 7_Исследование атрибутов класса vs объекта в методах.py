class Counter:
    total_counters = 0  # Атрибут класса

    def __init__(self, name):
        self.name = name
        self.value = 0  # Атрибут объекта
        Counter.total_counters += 1  # Увеличиваем общий счетчик

    def increment(self):
        # TODO: Увеличь self.value на 1
        self.value += 1


    def decrement(self):
        # TODO: Уменьши self.value на 1
        self.value -= 1


    def reset(self):
        # TODO: Установи self.value = 0
        self.value = 0


    def get_value(self):
        # TODO: Верни текущее значение счетчика
        return self.value

    # TODO: Создай метод get_total_counters() - возвращает количество всех счетчиков
    def get_total_counters(self):
        # Верни Counter.total_counters
        return Counter.total_counters

    # TODO: Создай метод get_info() - информация о счетчике
    def get_info(self):
        # Верни строку: "Счетчик {name}: {value} (всего счетчиков: {total_counters})"
        return f'Счетчик {self.name}: {self.value} (всего счетчиков: {Counter.total_counters})'

# Эксперимент:
print("=== Создаем счетчики ===")
counter1 = Counter("Первый")
counter2 = Counter("Второй")
counter3 = Counter("Третий")

print(f"Всего создано счетчиков: {counter1.get_total_counters()}")

print(f"\n=== Работаем с индивидуальными счетчиками ===")
counter1.increment()
counter1.increment()
counter1.increment()

counter2.increment()
counter2.increment()

counter3.increment()

print(counter1.get_info())
print(counter2.get_info())
print(counter3.get_info())

print(f"\n=== Сбрасываем первый счетчик ===")
counter1.reset()
print(counter1.get_info())
print(counter2.get_info())  # Не изменился!

print(f"\n=== Проверяем общий счетчик ===")
print(f"Через counter1: {counter1.get_total_counters()}")
print(f"Через counter2: {counter2.get_total_counters()}")
print(f"Через класс: {Counter.total_counters}")

# Вопросы для размышления:
# 1. Почему total_counters одинаковый для всех объектов?
# 2. Что произойдет если изменить Counter.total_counters = 100?
# 3. Почему сброс counter1 не повлиял на counter2?
