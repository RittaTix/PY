# set1, set2 = set(list(input())), set(list(input()))
# if set1.isdisjoint(set2):
#     print("NO")
# else:
#     print("YES")

# set1, set2 = set(input()), set(input())
# if set1.issuperset(set2):
#     print("YES")
# else:
#     print("NO")

# Ввод через списочное выражение int(i) for i in input().split()
# Не забываем sorted() и reverse
# для остального применил пересечение & и разницу - множеств...

# set1 = set([int(i) for i in input().split()])
# set2 = set([int(i) for i in input().split()])
# set3 = set([int(i) for i in input().split()])

# set1_set2 = set1&set2
# set4 = set1_set2-set3

# print(sorted(set4,reverse=True))

# set1 = set([int(i) for i in input().split()])
# set2 = set([int(i) for i in input().split()])
# set3 = set([int(i) for i in input().split()])

# my_set_iskl = set1&set2&set3
# my_set_vs = set1|set2|set3
# my_set_r = my_set_vs-my_set_iskl

# print(*sorted(my_set_r))

# set1 = set([int(i) for i in input().split()])
# set2 = set([int(i) for i in input().split()])
# set3 = set([int(i) for i in input().split()])

# set1_and_set2 = set1|set2
# only_set3 = set3 - set1_and_set2
# print(*sorted(only_set3,reverse=True))

set1 = set([int(i) for i in input().split()])
set2 = set([int(i) for i in input().split()])
set3 = set([int(i) for i in input().split()])
e = set(i for i in range(11))
print(*sorted(e-(set1|set2|set3)))