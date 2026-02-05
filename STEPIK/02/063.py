
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# for i in range(len(numbers)):
#     print(numbers[i])


# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# for num in numbers:
#     print(num)


# poets = [
#     ('Есенин', 13),
#     ('Тургенев', 14),
#     ('Маяковский', 28),
#     ('Лермонтов', 20),
#     ('Фет', 15),
# ]

# for i in range(len(poets)):
#     for j in range(i + 1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]

# print(poets[0])
# print(poets[-1])


# poets = [
#     ('Тургенев', 14),
#     ('Есенин', 13),
#     ('Маяковский', 28),
#     ('Фет', 15),
#     ('Лермонтов', 20),
# ]

# for i in range(len(poets)):
#     for j in range(i + 1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]

# print(poets[0])
# print(poets[-1])


# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# z = 1
# for num in numbers:
#     z *= num
# print(z)

# data = 'Python для продвинутых!'
# tmp = tuple(data) 
# print(tmp)

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# tmp = list(poet_data)
# poet_data = tuple(tmp[0:2]+['Москва'])
# print(poet_data)

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# tmp = list(numbers)
# sp = []
# for k in numbers:
#     sp.append(sum(k)/len(k))
# print((sp))

# a = (1,2,3)
# su = sum(a)
# print(su)

# a,b,c = int(input()),int(input()), int(input())
# х = -(b/(2*a))
# y = ((4*a*c-b**2)/(4*a))
# k = (х,y)
# print(k)

# n = int(input())
# students = [tuple(input().split()) for _ in range(n)]
# for i in students:
#     print(*i)
# print()
# for j in students:
#     if int(j[-1]) >=4:
#         print(*j)

# a, b, c = 10, 20, 30
# c, b, a = a + b, b*2, a + b + c

# print(a, b, c)

# points = [('матан', 100), ('линал', 98), ('ангем', 90)]
# subject, value = points[1]

# print(subject, value)

n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1,end = " ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3


    #a, b, c = b, c, a + b + c