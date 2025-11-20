# Создайте множество `colors = {"red", "blue", "green"}`.
# Добавьте новый цвет `"yellow"`.
# Удалите цвет `"blue"`.
# Попробуйте добавить уже существующий цвет `"red"` и объясните результат.

colors = {"red", "blue", "green"}
colors.add("yellow")
colors.remove("blue")
print(colors)

colors.add("red")
print(colors)