# TODO: Создай класс Pet (домашний питомец) с атрибутами:
# name = ""        (имя питомца)
# # animal_type = "" (тип животного: собака, кот, хомяк и т.д.)
# # age = 0          (возраст)
# # is_hungry = True (голоден ли питомец)

class Pet:
    name = ""
    animal_type = ""
    age = 0
    is_hungry = True



# TODO: Создай объект my_pet
my_pet = Pet()

# TODO: Присвой значения атрибутам:
my_pet.name = 'Murzik'
my_pet.age = 3
my_pet.animal_type = 'kot'
my_pet.is_hungry = False
# имя: "Мурзик", тип: "кот", возраст: 3, голоден: False

# TODO: Выведи информацию о питомце в формате:
# "Питомец Мурзик (кот, 3 года) - сытый" или "- голодный"

# Проверь себя:
print(f"Имя питомца: {my_pet.name}")
print(f"Тип: {my_pet.animal_type}")
print(f"Возраст: {my_pet.age}")
status = "сытый" if not my_pet.is_hungry else "голодный"
print(f"Статус: {status}")