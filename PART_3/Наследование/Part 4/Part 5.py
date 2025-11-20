# - Задание
# 5: Исследование MRO super()
# Поймем, как super() работает с порядком разрешения методов

class A:
    def method(self):
        print("Метод A")
        return "A"


class B(A):
    def method(self):
        print("Метод B")
        result = super().method()  # Какой метод вызовется?*
        return result + " -> B"


class C(A):
    def method(self):
        print("Метод C")
        result = super().method()  # Какой метод вызовется?*
        return result + " -> C"


class D(B, C):  # Множественное наследование*
    def method(self):
        print("Метод D")
        result = super().method()  # Какой метод вызовется?*
        return result + " -> D"

# Исследование:*
obj = D()

# 1. Посмотри на MRO класса D*
print("MRO класса D:", D.__mro__)

 # 2. Вызови метод и проследи порядок вызовов*
print("\nВызов obj.method():")
result = obj.method()
print(f"Итоговый результат: {result}")

# 3. Эксперимент: что будет, если изменить порядок наследования?*
class E(C, B):   # Поменяли местами C и B*


    def method(self):
        print("Метод E")
        result = super().method()
        return result + " -> E"


print("\n" + "=" * 50)
print("MRO класса E:", E.__mro__)
obj2 = E()
print("\nВызов obj2.method():")
result2 = obj2.method()
print(f"Итоговый результат: {result2}")

# Задания для размышления:
# 1. Почему порядок вызовов разный в D и E?
# 2. Какую роль играет super() в каждом классе?
# 3. Что было бы, если бы мы вызывали A.method(self) вместо super().method()? - попробуй*
