# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     x = (x1+x2)/2
#     y = (y1+y2)/2
#     return x,y

# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# # объявление функции
# def get_circle(radius):
#     import math
#     length = 2 * math.pi * radius
#     square = math.pi * (radius**2)

#     return length, square

# # считываем данные
# r = float(input())

# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)
    

from math import sqrt
# объявление функции
def solve(a, b, c):

    d = b**2-4*a*c

    if d==0:
        x1, x2 = (-b/(2*a)), (-b/(2*a))
        return x1, x2
    else:
        x1=(-b-sqrt(b**2-4*a*c))/(2*a)
        x2=(-b+sqrt(b**2-4*a*c))/(2*a)
        return min(x1,x2), max(x1,x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)