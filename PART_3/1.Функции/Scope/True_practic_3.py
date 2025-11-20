# Напишите функцию filter_list(data, threshold), которая принимает
# список чисел data и число threshold в качестве аргументов.
# Функция должна вернуть новый список, содержащий только те числа из data,
# которые больше или равны threshold

def filter_list(data, threshold):
    new_list = []
    for i in data:
        if i >= threshold:
            new_list.append(i)
    return new_list

data = [1, 5, 10, 2, 8, 12]
threshold = 7
result = filter_list(data, threshold)
print(result)

#Perplexity

def filter_list(data, threshold):
    return [x for x in data if x >= threshold]

data = [1, 5, 10, 2, 8, 12]
threshold = 7
result = filter_list(data, threshold)
print(result)