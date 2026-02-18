# a, b = int(input()), int(input())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print((a**10+b**10)**(0.5))

# m, r = float(input()), float(input())
# imt = m/(r*r)
# if imt < 18.5:
#     print("Недостаточная масса")
# elif imt > 25:
#     print("Избыточная масса")
# else:
#     print("Оптимальная масса")

# s = input()
# print(len(s)*60//100, "р.", len(s)*60%100, "коп.")

# s = input()
# print(len(s.split()))

# g = int(input())
# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
# print(animals[g%12])

# n = str(input())
# if len(n) == 6:
#     n = (n[0]+n[:-6:-1])
#     print(n.lstrip("0"))
# else:
#     n = (n[::-1])
#     print(n.lstrip("0"))


# '{:,}'.format(1234567890)
# '1,234,567,890'

# x = int(input())
# print(f"{x:,}")

# n, k = int(input()), int(input())
# ps, cur_idx = [x for x in range(1, n + 1)], 0
# while len(ps) > 1:
#     cur_idx = (cur_idx + k - 1) % len(ps)
#     del ps[cur_idx]

# print(ps[0])

