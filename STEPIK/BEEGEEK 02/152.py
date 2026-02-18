# def f(n=3):
#     return n + 7


# print(f(f(f())))

# def mean(*args):
#     sp = [i for i in args if type(i) == int or type(i) == float]
#     if len(sp) == 0:
#         return float(0)
#     else:
#         return sum(sp)/len(sp)


# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def greet(name, *args):
#     if len(args) == 0:
#         return f"Hello, {name}!"
#     else:
#         return f"Hello, {name} and {' and '.join(args)}!"

# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

# def print_products(*args):
#     z = 1
#     for i in args:
#         if type(i) is str and len(i) != 0:
#             print(f"{z}) {i}")
#             z+=1
#     if z == 1:
#         print("Нет продуктов")

# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '') 


# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(f"{key}: {value}")

# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 