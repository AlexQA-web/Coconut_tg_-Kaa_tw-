# 1. Напишите функцию `restore_health`, которая принимает два параметра:
#     - `current_health` — текущее здоровье героя.
#     - `potion` — количество здоровья, восстанавливаемое зельем.
# 2. Если восстановленное здоровье превышает максимум (`max_health = 100`), установите здоровье равным `100`.
# 3. Верните новое значение здоровья.

def restore_health(current_health, potion):
    restored_health = current_health + potion
    max_health = 100
    return max_health if restored_health >= max_health else restored_health

print(restore_health(90, 15))  # Вывод: 100
print(restore_health(50, 30))  # Вывод: 80