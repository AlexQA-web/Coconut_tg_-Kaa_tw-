class A:
    def method(self):
        return "Метод из A"

class B(A):
    # def method(self):
    #     return "Метод из B"
    pass

class C(B):
    def another_method(self):
        return "Метод из C"

# Создай объект класса C и исследуй:
obj = C()

# 1. Вызови obj.method() - какой результат?
print(obj.method())
# 2. Выведи C.__mro__ - что показывает?
print(C.__mro__)
# 3. Попробуй вызвать obj.another_method()
print(obj.another_method())
# 4. Есть ли у obj доступ к A.method()? No
# Эксперимент: временно закомментируй метод в классе B и посмотри, что изменится при вызове obj.method()