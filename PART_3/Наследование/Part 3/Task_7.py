class Product:
    def __init__(self, name, price, category):
        print(f"Инициализация Product: {name}")
        self.name = name
        self.price = price
        self.category = category
        self.id = f"{category}_{name.replace(' ', '_')}"

    def get_info(self):
        return f"{self.name} - {self.price}₽ (ID: {self.id})"


class Book(Product):
    def __init__(self, name, price, category, author, pages):
        # TODO: Инициализируй все атрибуты, дублируя код из родителя
        print(f"Инициализация Book: {name}")
        self.name = name
        self.price = price
        self.category = category
        self.id = f"{category}_{name.replace(' ', '_')}"  # Новые атрибуты:
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"{self.name} от {self.author} - {self.price}₽, {self.pages} стр."


# Тестирование:
book = Book("Python для начинающих", 1500, "programming", "Иван Иванов", 350)
print(book.get_info())

# Задания для размышления:
# 1. Сколько строк кода дублируется?
# 2. Что будет, если в родительском классе изменить логику создания ID?
# 3. Какие ошибки могут возникнуть при копировании кода?
# 4. Запомни эту проблему - в следующей главе изучим super()!