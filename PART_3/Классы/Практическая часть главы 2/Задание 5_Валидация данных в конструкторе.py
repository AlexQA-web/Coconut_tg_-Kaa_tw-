class Product:
    def __init__(self, name, price, category):
        if not name:
            self.name = 'Товар без названия'
        else:
            self.name = name

        if price < 0:
            self.price = 0
            print('Цена не может быть отрицательной!')
        else:
            self.price = price

        category_list = ["Электроника", "Одежда", "Книги", "Продукты"]
        if category not in category_list:
            self.category = 'Разное'
            print('Категория установлена как "Разное"!')
        else:
            self.category = category

        self.in_stock = True
        print(f"Создан товар: {self.name} - {self.price}₽ ({self.category})")

        # TODO: Добавь проверки:

        # 1. Имя не должно быть пустым, Если пустое - установи "Товар без названия"
        # 2. Цена не должна быть отрицательной, Если отрицательная - установи 0 и выведи предупреждение через print()
        # 3. Категория должна быть одной из: "Электроника", "Одежда", "Книги", "Продукты", Если другая - установи "Разное" и выведи предупреждение через print()




# TODO: Протестируй валидацию:

# Нормальный товар
product1 = Product("iPhone 15", 120000, "Электроника")

# Пустое название
product2 = Product("", 50000, "Электроника")

# Отрицательная цена
product3 = Product("Футболка", -500, "Одежда")

# Неизвестная категория
product4 = Product("Молоток", 1500, "Инструменты")

# Несколько проблем сразу
product5 = Product("", -100, "Неизвестно")

# Проверь результаты:
products = [product1, product2, product3, product4, product5]
for prod in products:
    print(f"Товар: {prod.name} - {prod.price}₽ ({prod.category})")