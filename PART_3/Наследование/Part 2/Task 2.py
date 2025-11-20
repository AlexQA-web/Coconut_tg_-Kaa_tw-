class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return f"{self.name} работает как {self.position}"


class Programmer(Employee):
    # TODO: Добавь методы:
    # - code() - возвращает "{name} пишет код"
    def code(self):
        return f'{self.name} пишет код'
    # - debug() - возвращает "{name} ищет баги"
    def debug(self):
        return f'{self.name} ищет баги'
    # - commit() - возвращает "{name} делает коммит в Git"
    def commit(self):
        return f'{self.name} делает коммит в Git'


class Designer(Employee):
    # TODO: Добавь методы:
    # - design() - возвращает "{name} создает дизайн"
    def design(self):
        return f'{self.name} создает дизайн'
    # - prototype() - возвращает "{name} делает прототип"
    def prototype(self):
        return f'{self.name} делает прототип'
    # - present() - возвращает "{name} презентует идею"
    def present(self):
        return f'{self.name} презентует идею'


# Протестируй все методы:
prog = Programmer("Анна", "Python разработчик")
designer = Designer("Петр", "UI/UX дизайнер")

# Убедись, что у каждого объекта работают:
# 1. Унаследованный метод work()
print(prog.work())
print(designer.work())
# 2. Все собственные методы
print(prog.code())
print(prog.debug())
print(prog.commit())
print(designer.design())
print(designer.present())
print(designer.prototype())
# 3. Проверь доступ к атрибутам name и position
print(prog.name)
print(prog.position)
print(designer.name)
print(designer.position)