# myset = set()
# item = myset.pop()

# print(item)

# myset = set()
# for i in range(10):
#     if i % 2 == 0:
#         myset.add('even')
#     else:
#         myset.add('odd')

# print(len(myset))

# for i in range(int(input())):
#     print(len(set(input().lower())))

# s = ""
# for i in range(int(input())):
#     s+=input().lower()
# print(len(set(s)))

# string = input().lower()
# sp = string.split()
# m = set()
# for i in range(len(sp)):
#     m.add((sp[i]).strip('.,;:-?!'))
# print(len(m))


# string = input().split()
# m = set()
# for i in range(len(string)):
#     if int(string[i]) not in m:
#         print("NO")
#         m.add(int(string[i]))
#     else:
#        print("YES") 

# sp = []
# usp = 0
# z = set()
# n = int(input())
# for i in range(n):
#     s = input().split(":")
#     if (s[1] == " Correct") and (s[0] not in z):
#         usp +=1
#         z.add(s[0])
#     s = s[0]
#     sp.append(s)
# m = set(sp)
# print(z)
# print(m)

# if usp == 0:
#     print("Вы можете стать первым, кто решит эту задачу")
# else:
#     print("Верно решили",usp,"учащихся")
#     print("Из всех попыток ",round(len(m)/n*100), "% верных", sep = "")


sp = []
z = set()
usp = 0
m = 0
n = int(input())
for i in range(n):
    s = input().split(":")
    if (s[1] == " Correct") and (s[0] not in z):
        usp +=1
        z.add(s[0])
    if (s[1] == " Correct"):
        m+=1


if usp == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    print("Верно решили",usp,"учащихся")
    print("Из всех попыток ",round(m/n*100), "% верных", sep = "")