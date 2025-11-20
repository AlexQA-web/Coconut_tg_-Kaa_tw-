class Product:
    name = ""
    price = 0.0
    category = ""
    in_stock = True
    quantity = 0

# TODO: Создай список товаров для интернет-магазина
products = []

product_1 = Product()
product_1.name = 'Ноутбук ASUS'
product_1.price = 75000.0
product_1.category = 'Электроника'
product_1.in_stock = True
product_1.quantity = 3
products.append(product_1)

product_2 = Product()
product_2.name = 'Мышь Logitech'
product_2.price = 2500.0
product_2.category = 'Электроника'
product_2.in_stock = True
product_2.quantity = 15
products.append(product_2)

product_3 = Product()
product_3.name = 'Книга Python'
product_3.price = 1200.0
product_3.category = 'Книги'
product_3.in_stock = False
product_3.quantity = 0
products.append(product_3)

product_4 = Product()
product_4.name = 'Кофе Арабика'
product_4.price = 800.0
product_4.category = 'Продукты'
product_4.in_stock = True
product_4.quantity = 25
products.append(product_4)

product_5 = Product()
product_5.name = 'Телефон iPhone'
product_5.price = 120000.0
product_5.category = 'Электроника'
product_5.in_stock = True
product_5.quantity = 2
products.append(product_5)
"""
TODO: Создай и добавь в список 5 товаров:
Товар 1: "Ноутбук ASUS", 75000.0, "Электроника", True, 3
Товар 2: "Мышь Logitech", 2500.0, "Электроника", True, 15  
Товар 3: "Книга Python", 1200.0, "Книги", False, 0
Товар 4: "Кофе Арабика", 800.0, "Продукты", True, 25
Товар 5: "Телефон iPhone", 120000.0, "Электроника", True, 2
"""

# TODO: Выведи каталог всех товаров
print("=== КАТАЛОГ ТОВАРОВ ===")
count = 1
for product in products:
    print(f'Товар {count}: {product.name},цена {product.price} руб.,категория товара: "{product.category}",',
          f'в наличии: {product.quantity} шт.' if product.in_stock else 'нет в наличии.'
         )
    count += 1


# TODO: Найди и выведи только товары в категории "Электроника"
print("=== КАТАЛОГ ТОВАРОВ категории Электроника ===")
count = 1
for product in products:
   if product.category == 'Электроника':
        print(f'Товар {count}: {product.name},цена {product.price} руб.,категория товара: "{product.category}",',
              f'в наличии: {product.quantity} шт.' if product.in_stock else 'нет в наличии.'
              )
        count += 1

# TODO: Найди товары дороже 10000₽
print("\n=== ДОРОГИЕ ТОВАРЫ (>10000₽) ===")
count = 1
for product in products:
    if product.price > 100000.0:
        print(f'Товар {count}: {product.name},цена {product.price} руб.,категория товара: "{product.category}",',
              f'в наличии: {product.quantity} шт.' if product.in_stock else 'нет в наличии.'
              )
        count += 1

# TODO: Посчитай общую стоимость всех товаров в наличии
total_value = 0
for product in products:
    if product.in_stock:
        total_value += product.price


print(f"\n=== СТАТИСТИКА ===")
print(f"Общая стоимость товаров в наличии: {total_value}₽")