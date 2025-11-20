class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"{self.name} - {self.price}₽ ({self.category})"


class Electronics(Product):
    # TODO: Добавь методы:
    # - check_warranty() - возвращает "Гарантия действительна"
    @staticmethod
    def check_warranty():
        return 'Гарантия действительна'
    # - power_on() - возвращает "{name} включается"
    def power_on(self):
        return f'{self.name} включается'


class Clothing(Product):
    # TODO: Добавь методы:
    # - try_on() - возвращает "Примерка {name}"
    def try_on(self):
        return f'Примерка {self.name}'
    # - wash_instructions() - возвращает "Стирать при 30°C"
    @staticmethod
    def wash_instructions():
        return 'Стирать при 30°C'


class Book(Product):
    # TODO: Добавь методы:
    # - read_sample() - возвращает "Читаем отрывок из {name}"
    def read_sample(self):
        return f'Читаем отрывок из {self.name}'
    # - bookmark() - возвращает "Закладка добавлена в {name}"
    def bookmark(self):
        return f'Закладка добавлена в {self.name}'

# Создай по одному объекту каждого типа и протестируй все методы

phone = Electronics('Iphone 17', 2499, 'phones')
shirt = Clothing('Hawaii', 35, 'shirts')
book = Book('451F', 15, 'utopy')

print(phone.get_info())
print(shirt.get_info())
print(book.get_info())

print(phone.check_warranty())
print(phone.power_on())

print(shirt.try_on())
print(shirt.wash_instructions())

print(book.bookmark())
print(book.read_sample())

