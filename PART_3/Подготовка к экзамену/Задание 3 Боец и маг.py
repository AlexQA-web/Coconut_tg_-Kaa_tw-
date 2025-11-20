# 1. Создайте базовый класс `Hero` с атрибутами:
#     - `name` (имя героя).
#     - `health` (здоровье).
#     - Метод `take_damage`, который уменьшает здоровье на указанное значение.
# 2. Создайте два дочерних класса:
#     - `Warrior` с методом `attack`, который возвращает "Нанёс 20 урона мечом".
#     - `Mage` с методом `attack`, который возвращает "Нанёс 15 урона заклинанием".
# 3. Создайте объекты `Warrior` и `Mage` и вызовите их методы.


class Hero:
    def __init__(self, name: object, health: object) -> None:
        self.name = name
        self.health = health
        
    def take_damage(self, damage):
        self.health -= damage
        
class Warrior(Hero):
    def attack(self):
        return f'{self.name} Нанёс 20 урона мечом'
    
    
class Mage(Hero):
    def attack(self):
        return f'{self.name} Нанёс 15 урона заклинанием'


warrior = Warrior("Тралл", 120)
mage = Mage("Джайна", 80)

print(warrior.attack())  # Вывод: Нанёс 20 урона мечом
print(mage.attack())     # Вывод: Нанёс 15 урона заклинанием