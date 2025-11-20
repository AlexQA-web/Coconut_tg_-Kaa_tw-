# # Написать функцию calculate_delivery_cost(weight, distance, fragile=False),
# # которая рассчитывает стоимость доставки посылки.
# #
# # - weight (число): вес посылки в кг.
# # - distance (число): расстояние доставки в км.
# # - fragile (булево, по умолчанию False): является ли посылка хрупкой.
# #
# # Правила расчета:
# #
# # - Базовая стоимость: 10 рублей за кг + 5 рублей за км.
# # - Если посылка хрупкая, стоимость увеличивается на 50%.
# # - Минимальная стоимость доставки: 200 рублей.
# #
# # Функция должна возвращать стоимость доставки
#
def calculate_delivery_cost(weight, distance, fragile=False):
    price_for_kilogram = 10
    price_per_1_km = 5
    min_price_for_order = 200
    base_price = (weight * price_for_kilogram) + (distance * price_per_1_km)
    base_price_fragile = base_price * 1.5

    if base_price > min_price_for_order and fragile == False:
        return base_price
    if fragile:
        if base_price > min_price_for_order or base_price_fragile > min_price_for_order:
            return base_price_fragile
        else:
            return None
    else:
        return min_price_for_order

print(calculate_delivery_cost(2, 2))   # Print 200
print(calculate_delivery_cost(20, 20)) # Print 300
print(calculate_delivery_cost(10, 10, True))



def calculate_delivery_cost(weight, distance, fragile=False):
    PRICE_PER_KG = 10
    PRICE_PER_KM = 5
    MIN_ORDER_PRICE = 200
    FRAGILE_MULTIPLIER = 1.5

    base_price = (weight * PRICE_PER_KG) + (distance * PRICE_PER_KM)

    if fragile:
        base_price *= FRAGILE_MULTIPLIER

    return max(base_price, MIN_ORDER_PRICE)


print(calculate_delivery_cost(2, 2))  # Print 200
print(calculate_delivery_cost(20, 20))  # Print 300
print(calculate_delivery_cost(10, 10, True))  # Print 300
