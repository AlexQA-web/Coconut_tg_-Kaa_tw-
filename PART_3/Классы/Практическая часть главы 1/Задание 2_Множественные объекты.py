class Smartphone:
    brand = ""
    model = ""
    storage = 0  # объем памяти в GB
    battery = 100  # заряд батареи в %
    is_on = False  # включен ли телефон

    # TODO: Создай три разных телефона:


phone1 = Smartphone()
phone2 = Smartphone()
phone3 = Smartphone()

# TODO: Настрой первый телефон:
phone1.brand = 'Apple'
phone1.model = 'iPhone 15'
phone1.storage = 128
phone1.battery = 85
phone1.is_on = True
# brand="Apple", model="iPhone 15", storage=128, battery=85, is_on=True
# TODO: Настрой второй телефон:
phone2.brand = 'Samsung'
phone2.model = 'Galaxy S24'
phone2.storage = 256
phone2.battery = 92
phone2.is_on = False
# brand="Samsung", model="Galaxy S24", storage=256, battery=92, is_on=False
# TODO: Настрой третий телефон:
phone3.brand = 'Xiaomi'
phone3.model = 'Mi 13'
phone3.storage = 128
phone3.battery = 67
phone3.is_on = True
# brand="Xiaomi", model="Mi 13", storage=128, battery=67, is_on=True

# TODO: Выведи информацию о каждом телефоне в формате:
# "Apple iPhone 15 (128GB) - Заряд: 85%, Включен"
# используя цикл

phones = [phone1, phone2, phone3]
for phone in phones:
    print(f'{phone.brand} {phone.model} ({phone.storage}GB) - Заряд: {phone.battery}%,', 'Включен' if phone.is_on else 'Выключен')