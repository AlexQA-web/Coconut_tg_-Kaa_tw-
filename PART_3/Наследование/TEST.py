class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.employee_id = None

    def get_info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.salary}"

    def work(self):
        return f"{self.name} работает"


# Создаем дочерний класс
class Developer(Employee):
    def code(self):
        return f"{self.name} пишет код"


class Manager(Employee):
    def manage(self):
        return f"{self.name} управляет командой"

dev = Developer("Анна", 80000)
print(dev.get_info())  # Метод родителя!
print(dev.work())      # Метод родителя!
print(dev.code())      # Собственный метод

manager = Manager("Петр", 90000)
print(manager.get_info())  # Метод родителя!
print(manager.manage())    # Собственный метод