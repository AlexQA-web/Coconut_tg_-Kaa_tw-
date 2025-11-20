class Product:  # Объявляем класс товара Product
    def __init__(self, name, price, category, stock):  # Конструктор: принимает имя, цену, категорию и остаток
        self.name = name  # Сохраняем имя товара
        self.price = price  # Сохраняем цену товара
        self.category = category  # Сохраняем категорию товара
        self.stock = stock  # Сохраняем количество на складе

    def get_info(self):  # Метод: вернуть строку с краткой информацией о товаре
        return f"{self.name} ({self.category}) — {self.price} ₽, на складе: {self.stock}"  # Формируем и возвращаем строку-описание

    def is_available(self):  # Метод: проверить, есть ли товар в наличии
        return self.stock > 0  # Возвращаем True, если на складе больше 0, иначе False

    def reduce_stock(self, amount):  # Метод: уменьшить остаток на складе на указанную величину
        self.stock -= amount  # Вычитаем amount из текущего stock

    def add_stock(self, amount):  # Метод: увеличить остаток на складе на указанную величину
        self.stock += amount  # Прибавляем amount к текущему stock


class ShoppingCart:  # Объявляем класс корзины ShoppingCart
    def __init__(self, customer_name):  # Конструктор: принимает имя покупателя
        self.customer_name = customer_name  # Сохраняем имя покупателя
        self.items = {}  # Инициализируем словарь товаров в корзине формата {Product: quantity}
        self.total_amount = 0.0  # Инициализируем общую сумму корзины как число с плавающей точкой

    def add_item(self, product, quantity):  # Метод: добавить товар в корзину
        self.items[product] = self.items.get(product, 0) + quantity  # Увеличиваем количество по ключу product на quantity
        self.calculate_total()  # Пересчитываем общую сумму корзины после добавления

    def remove_item(self, product_name):  # Метод: удалить товар из корзины по названию
        for p in list(self.items.keys()):  # Итерируемся по копии ключей словаря items
            if p.name == product_name:  # Если имя товара соответствует переданному имени
                self.items.pop(p)  # Удаляем товар из корзины
                break  # Прерываем цикл после удаления
        self.calculate_total()  # Пересчитываем общую сумму после изменения состава корзины

    def calculate_total(self):  # Метод: пересчитать общую сумму корзины
        self.total_amount = sum(p.price * qty for p, qty in self.items.items())  # Суммируем price * quantity по всем позициям
        return self.total_amount  # Возвращаем вычисленную сумму

    def get_cart_info(self):  # Метод: вернуть текстовую информацию о содержимом корзины
        if not self.items:  # Если корзина пустая
            return f"Корзина {self.customer_name}: пусто, сумма 0 ₽"  # Возвращаем строку про пустую корзину
        lines = [f"Корзина {self.customer_name}:"]  # Начинаем список строк с заголовка, содержащего имя покупателя
        for p, qty in self.items.items():  # Итерируемся по парам (товар, количество) в корзине
            lines.append(f"- {p.name} x {qty} = {p.price * qty} ₽")  # Добавляем строку с позицией и её стоимостью
        lines.append(f"Итого: {self.total_amount} ₽")  # Добавляем строку с итоговой суммой
        return "\n".join(lines)  # Склеиваем строки в один многострочный текст и возвращаем его

    def checkout(self):  # Метод: оформить заказ
        for p, qty in self.items.items():  # Проходим по всем позициям в корзине
            p.reduce_stock(qty)  # Уменьшаем складской остаток товара на количество из корзины
        self.items.clear()  # Очищаем корзину после оформления
        self.calculate_total()  # Пересчитываем сумму (становится 0 после очистки)
        return True  # Возвращаем признак успешного оформления



# TODO: Создай классы Product и ShoppingCart полностью самостоятельно

# Тестирование должно работать примерно так:

# Создаем товары
laptop = Product("Ноутбук", 75000, "Электроника", 5)
mouse = Product("Мышь", 2500, "Электроника", 20)
book = Product("Python для начинающих", 1200, "Книги", 10)

# Создаем корзину
cart = ShoppingCart("Анна Петрова")

print("=== Добавляем товары в корзину ===")
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(book, 3)

print(cart.get_cart_info())

print(f"\n=== Общая сумма ===")
total = cart.calculate_total()
print(f"К оплате: {total}₽")

print(f"\n=== Оформляем заказ ===")
cart.checkout()

print(f"\n=== Проверяем остатки на складе ===")
print(laptop.get_info())
print(mouse.get_info())
print(book.get_info())
