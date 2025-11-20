class A:
    def method(self):
        return "Метод A"

    def only_a(self):
        return "Только в A"


class B(A):
    # def method(self):
    #     return "Метод B"

    def only_b(self):
        return "Только в B"


class C(B):
    def only_c(self):
        return "Только в C"


# Эксперименты:
obj = C()

# 1. Какой метод вызовется?
print("1.", obj.method())
# 2. Проверь MRO
print("2. MRO:", C.__mro__)

# 3. Доступны ли методы из всех классов?
print("3a.", obj.only_a())
print("3b.", obj.only_b())
print("3c.", obj.only_c())

# 4. Эксперимент: временно закомментируй метод method() в классе B
# и запусти снова obj.method(). Что изменится?
# 5. Проверь, есть ли у C собственный метод method():
print("4. Есть ли C.method?", hasattr(C, 'method'))
print("5. Откуда метод?", obj.method.__qualname__)