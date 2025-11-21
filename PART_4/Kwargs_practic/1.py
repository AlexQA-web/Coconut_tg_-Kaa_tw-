
def greet(greeting, **kwargs):
    for key, value in kwargs.items():
        print(f'{greeting}, {value}!')

greet(greeting='Здарова', name_1='Корова', name_2='Петрова', name_3='Иванова')


def create_dict(**kwargs):
    return kwargs

print(create_dict(name='Al', name_2= 'Sal'))



