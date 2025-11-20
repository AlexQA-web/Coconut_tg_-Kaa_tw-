class Book:
    title = ""
    author = ""
    pages = 0
    isbn = ""


# Эксперимент 1: Создаем два одинаковых объекта
book1 = Book()
book1.title = "Война и мир"
book1.author = "Толстой"
book1.pages = 1300
book1.isbn = "978-5-389-07260-3"

book2 = Book()
book2.title = "Война и мир"
book2.author = "Толстой"
book2.pages = 1300
book2.isbn = "978-5-389-07260-3"

print("=== Эксперимент 1: Сравнение объектов ===")
print(f"book1 == book2: {book1 == book2}")  # Что покажет?

# Эксперимент 2: Присваивание объекта
book3 = book1  # book3 ссылается на тот же объект, что и book1

print("\n=== Эксперимент 2: Ссылки на объекты ===")
print(f"book1 is book3: {book1 is book3}")  # Что покажет?

# Изменяем book3
book3.title = "Анна Каренина"
print(f"После изменения book3.title:")
print(f"book1.title: {book1.title}")  # Что покажет?
print(f"book3.title: {book3.title}")  # Что покажет?
# TODO: Подумай над следующим:
# 1. Почему book1 == book2 дает False, хотя содержимое одинаковое Потому что это разные объекты и хранятся в разных ячейках памяти
# 2. Почему изменение book3.title изменило book1.title Потому что book3 и book1 ссылаются на одну ячейку в памяти

print("\n=== ID объектов ===")
print(f"ID book1: {id(book1)}")
print(f"ID book2: {id(book2)}")
print(f"ID book3: {id(book3)}")