# n,m,k,p = (int(input()) for i in range(4))
# skolko_ne_vypolnilo = m|k
# bez_dublei = skolko_ne_vypolnilo|p
# it = n-bez_dublei
# print(n)

# s = input().split()
# m = {i for i in s}
# print(len(s) - len(m))

# n = int(input())
# m = {i for i in range(n)}
# if n == len(m):
#     print("OK")
# else:
#     print("REPEAT")

# m,n = int(input()), int(input())
# m_dom = {input() for i in range(m)}
# for j in range(n):
#     if input() in m_dom:
#         print("YES")
#     else:
#         print("NO")

# set1, set2 = set(input().split()), set(input().split())
# set1_z = {int(d) for d in set1}
# set2_z = {int(d) for d in set2}
# set3 = set1_z&set2_z
# if set3!=set():
#     print(*sorted(set3, reverse=True))
# else:
#     print("BAD DAY")

# set1, set2 = set(input().split()), set(input().split())

# if set1 == set2:
#     print("YES")
# else:
#     print("NO")    

# m, n = int(input()), int(input())
# mathematics_pupil = {input() for _ in range(m)}
# informatics_pupil = {input() for _ in range(n)}
# difference = mathematics_pupil^informatics_pupil
# print(m-(len(difference)))

# put your python code here
# m, n = int(input()), int(input())
# mathematics_pupil = {input() for _ in range(m)}
# informatics_pupil = {input() for _ in range(n)}
# difference = mathematics_pupil^informatics_pupil
# if (len(difference)) == 0:
#     print("NO")
# else:
#     print(len(difference))

# s1, s2 = set(input().split()), set(input().split())
# s3 = s1|s2
# print(*sorted(s3))

# m, n = int(input()), int(input())
# sp = [input() for i in range(m+n)]
# mn = set()
# for j in sp:
#     if j in mn:
#         mn.add(j)
#     else:
#         mn.remove(j)
# if len(mn)>0:
#     print(len(mn))
# else:
#     print("NO")

m = int(input())
n = int(input())
first_set = set([input() for _ in range(n)])
empty_set = set()
if m == 1: 
    print(*sorted(first_set))
else:
    for i in range(m-1): 
        for j in range (int(input())):
            empty_set.add(input()) 
        first_set.intersection_update(empty_set) 
        empty_set.clear()
    first_set = sorted(first_set)
    for row in first_set:
        print(row)

