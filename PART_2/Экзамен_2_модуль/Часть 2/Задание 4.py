# Напишите программу, которая:
# Создаёт строку `quote = "Python is easy and powerful!"`.
# Заменяет `easy` на `fun` и `powerful` на `versatile`.
# Выводит результат.

quote = "Python is easy and powerful!"
modified_quote = quote.replace("powerful", "versatile").replace("easy", "fun")
print(modified_quote)