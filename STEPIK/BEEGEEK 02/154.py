#numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

# words = ['this', 'is', 'a', 'test', 'of', 'sorting']
# words.sort(key=len)
# print(words)

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

# def compare_by_sr_arifm(p):
#     return sum(p)/len(p)

# numbers.sort(key=compare_by_sr_arifm)
# print(numbers[0])
# print(numbers[-1])


# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# from math import sqrt
# def rasstoyanie(r):
#     return sqrt(r[0]**2 + r[1]**2)
# print(sorted(points, key=rasstoyanie))

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# def raschet(r):
#     return min(r) + max(r)

# print(sorted(numbers, key=raschet))


# def f1(x):
#     return 2*x+1


# def f2(x):
#     return x**2


# def f3(x):
#     return -x**2+1


# def f4(x):
#     return x-3


# funcs = [f1, f2, f3, f4]
# i = int(input())
# print(funcs[i](2))





# def comparator(item):
#     return item[0]


# data = [('red', 1), ('blue', 2), ('green', 5), ('blue', 1)]
# data.sort(key=comparator)   # сортируем по первому полю

# print(data)

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

# def comparator(elem):
#     return elem[i-1] 

# i = int(input())
# for z in sorted(athletes,key=comparator):
#     print(*z)

# import math

# n,imya = int(input()), input()

# def f1():
#     print(n**2)

# def f2():
#     print(n**3)

# def f3():
#     print(math.sqrt(n))

# def f4():
#    print(abs(n))

# def f5():
#     print(math.sin(n))


# d = {'квадрат': f1 , 'куб': f2,'корень': f3,'модуль': f4,'синус': f5}
# d[imya]()

# квадрат: функция принимает число и возвращает его квадрат;
# куб: функция принимает число и возвращает его куб;
# корень: функция принимает число и возвращает корень квадратный из этого числа;
# модуль: функция принимает число и возвращает его модуль;
# синус: функция принимает число (в радианах) и возвращает синус этого числа.

# def start():
#     # тело функции start
#     pass


# def stop():
#     # тело функции stop
#     pass


# def pause():
#     # тело функции pause
#     pass


# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция

# command = input()  # считываем название команды

# commands[command]()  # вызываем нужную функцию через словарь по ключу

sp = '12 14 79 7 4 123 45 90 111'.split()

def comparator(r):
    s = 0
    for i in r:
        s += int(i)
    return s

print(sorted(sp, key=comparator))