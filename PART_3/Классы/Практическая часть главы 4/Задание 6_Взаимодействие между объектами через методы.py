class Player:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.is_alive = True

    # TODO: Создай метод attack(target) - атака другого игрока
    def attack(self, target):
        # 1. Проверь что self.is_alive == True
        if self.is_alive:
        # 2. Проверь что target.is_alive == True
            if target.is_alive:
                # 3. Выведи сообщение "{self.name} атакует {target.name}!"
                print(f'{self.name} атакует {target.name}!')
                # 4. Вызови target.take_damage(self.attack_power)
                target.take_damage(self.attack_power)
                # 5. Верни True если атака прошла, False если нет
                return True
        return False


    # TODO: Создай метод take_damage(damage) - получение урона
    def take_damage(self, damage):
        # 1. Уменьши self.health на damage
        self.health -= damage
        # 2. Если health <= 0, установи health = 0 и is_alive = False
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
        # 3. Выведи сообщение о получении урона и текущем здоровье
            print(f'Игрок получил {damage} урона и его здоровье опустилось до {self.health}')
        # 4. Если игрок умер, выведи сообщение о смерти
            print('Игрок умер!')


    # TODO: Создай метод heal(amount) - лечение
    def heal(self, amount):
        # 1. Проверь что игрок жив
        if self.is_alive:
            # 2. Увеличь health на amount, но не больше max_health
            self.health += amount
            # 3. Выведи сообщение о лечении
            print(f'Вы восстановили здоровье на {amount} единиц.')
            # 4. Верни реально восстановленное здоровье
            print(f'Ваше текущее здоровье {self.health} единиц')
            return amount


    # TODO: Создай метод get_status() - статус игрока
    def get_status(self):
        # Верни строку: "{name}: {health}/{max_health} HP, {'жив' if is_alive else 'мертв'}"
        return f'{self.name}: {self.health}/{self.max_health} HP, {'жив' if self.is_alive else 'мертв'}'
        pass

# Тестирование боя:
warrior = Player("Воин", 120, 25)
mage = Player("Маг", 80, 30)

print("=== Начало боя ===")
print(warrior.get_status())
print(mage.get_status())

print(f"\n=== Раунд 1 ===")
warrior.attack(mage)
print(mage.get_status())

print(f"\n=== Раунд 2 ===")
mage.attack(warrior)
print(warrior.get_status())

print(f"\n=== Маг лечится ===")
healed = mage.heal(20)
print(f"Восстановлено {healed} HP")
print(mage.get_status())

print(f"\n=== Раунд 3 ===")
warrior.attack(mage)
mage.attack(warrior)

print(f"\n=== Итоговые статусы ===")
print(warrior.get_status())
print(mage.get_status())
