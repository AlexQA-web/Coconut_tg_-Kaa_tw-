class Employee:
    def __init__(self, first_name, last_name, birth_year, department):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.department = department

        # TODO: Создай дополнительные атрибуты:

        # 1. full_name = имя + фамилия
        self.full_name = first_name + ' ' + last_name

        # 2. age = текущий год (2024) - год рождения
        self.age = 2025 - birth_year

        # 3. employee_id = первые 2 буквы имени + первые 2 буквы фамилии + год рождения# Например: "Анна Петрова 1990" -> "АНПЕ1990"
        self.employee_id = first_name[0:2].upper() + last_name[0:2].upper() + str(birth_year)

        # 4. email = имя.фамилия@компания.ru (все в нижнем регистре)
        self.email = first_name.lower() + '.' + last_name.lower() + '@' + department.lower() + '.ru'

        # 5. is_senior = True если возраст >= 30, иначе False
        self.is_senior = True if self.age >= 30 else False

        print(f"Зарегистрирован сотрудник: {self.full_name}")
        print(f"ID: {self.employee_id}, Email: {self.email}")
        print(f"Возраст: {self.age}, Статус: {'Senior' if self.is_senior else 'Junior'}")


# TODO: Создай сотрудников:
emp1 = Employee("Анна", "Петрова", 1990, "IT")
emp2 = Employee("Петр", "Иванов", 2000, "HR")
emp3 = Employee("Мария", "Сидорова", 1985, "Finance")

# Проверь генерацию атрибутов:
employees = [emp1, emp2, emp3]
for emp in employees:
    print(f"\n{emp.full_name} ({emp.age} лет)")
    print(f"Отдел: {emp.department}")
    print(f"Email: {emp.email}")
    print(f"Статус: {'Senior' if emp.is_senior else 'Junior'}")