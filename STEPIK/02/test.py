# s = input().split()
# print(type(s))

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# print(type(temp))

# p = input()
# b = 'abcdefgh'
# p = str(int(b.find(p[0]))+1) + p[1]
# print(p)

# n = int(input())
# # sp = list(range(1,n**2+1))
# # print(sp)


# matrix = []
# sum = 0
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# # print((matrix[0]))
# # print(type(matrix[0]))
# list = (matrix[0])
# columns = [sum(col) for col in zip(*list)]
# print(columns)




# if "Correct" in set("Поколение Python: Correct"):
#     print(set("Поколение Python: Correct"))

# print(set("Поколение Python: Correct".split()))

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

for i in users:
    print(i['phone'][-1])