# Напиcать функцию string_length(s), которая принимает строку в качестве аргумента
# и возвращает ее длину.


def string_length(s):
    return len(s)

print(string_length("Hello"))      # Должно вывести: 5
print(string_length("Python is fun")) # Должно вывести: 13
print(string_length(""))           # Должно вывести: 0