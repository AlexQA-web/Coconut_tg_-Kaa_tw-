class Movie:
    title = ""
    year = 0
    genre = ""
    rating = 0.0

# Создаем фильм
movie = Movie()
movie.title = "Матрица"
movie.year = 1999
movie.genre = "Фантастика"
movie.rating = 8.7

# Эксперименты с ошибками:
# 1. Попробуй обратиться к несуществующему атрибуту:
# 2. Попробуй обхект movie вызвать как функцию
# 2.1. Попробуй аттрибут вызвать как функцию: print(movie.title()) и ознакомся с ошибкой
# 3. Попробуй обратиться к атрибуту класса, а не объекта (то есть через сам класс)
# 4. Попробуй создать объект без вызова класса. То есть по сути в переменную положить сам класс
    # movie1 = Movie
    # print(movie1 == Movie)

# print(movie.duration)  # AttributeError: 'Movie' object has no attribute 'duration'
# movie() # TypeError: 'Movie' object is not callable
# print(movie.genre())  # TypeError: 'str' object is not callable
# print(Movie.genre) # Код ничего не выводит

# cinema = Movie
# print(cinema == Movie)   # True
