# 1. Создать класс `Book` с атрибутами `title` (название), `author` (автор) и `pages` (количество страниц)
# 2. Сделать на его основе объект
# 3. Вывести при помощи `print()` атрибуты этого объекта
# 4. После изменить для конкретного объекта title и вывести его, дабы убедиться что он изменился.
# 5. Добавить новый атрибут объекту и тоже его вывести при помощи `print()`

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


book_1 = Book('Freedom', 'J.F. King', 999)
print(book_1.__dict__)

book_1.title = 'Aldente'
book_1.colour = 'Red'
print(book_1.__dict__)