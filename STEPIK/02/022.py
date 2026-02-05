# n = int(input())
# che1, che2, che3, che4 = 0, 0, 0, 0 
# for i in range (n):
#     s = input().split()
#     if int(s[0]) < 0 and int(s[1]) > 0:
#         che2+=1
#     if int(s[0]) > 0 and int(s[1]) > 0:
#         che1+=1
#     if int(s[0]) < 0 and int(s[1]) < 0:
#         che3+=1
#     if int(s[0]) > 0 and int(s[1]) < 0:
#         che4+=1
# print("Первая четверть:", che1)
# print("Вторая четверть:", che2)
# print("Третья четверть:", che3)
# print("Четвертая четверть:", che4)


# sp = input().split()
# count = 0
# for i in range(len(sp)):
#     if i < len(sp)-1:
#         if int(sp[i]) < int(sp[i+1]):
#             count += 1
# print(count)


# sp = input().split()

# for i in range(0, len(sp)-1, 2):
#     sp[i], sp[i+1] = sp[i+1], sp[i]

# print(*sp)

# sp = input().split()
# print(sp[-1],*sp[:-1])

# sp2 = []
# count = 0
# sp1 = input().split()

# for i in range(len(sp1)):
#     if sp1[i] not in sp2:
#         sp2.append(sp1[i])
#         count += 1

# print(count)

# n = int(input())
# sp = []
# flag = False
# for i in range(n):
#     sp.append(int(input()))
# it = int(input())

# for i in range(len(sp)):
#     for j in range(len(sp)):
#         if i != j:
#             if sp[i]*sp[j] == it:
#                 flag = True
#                 break
# if flag == False:
#     print("НЕТ")
# else:
#     print("ДА")


# s1, s2 = input(), input()
# if s1 == s2:
#     print("ничья")
# elif s1 == "камень" and s2 == "ножницы":
#     print("Тимур")
# elif s1 == "ножницы" and s2 == "бумага":
#     print("Тимур")
# elif s1 == "бумага" and s2 == "камень":
#     print("Тимур")
# else:
#     print("Руслан")

# s1, s2 = input(), input()
# if s1 == s2:
#     print("ничья")
# elif s1 == "камень" and s2 == "ножницы":
#     print("Тимур")
# elif s1 == "ножницы" and s2 == "бумага":
#     print("Тимур")
# elif s1 == "бумага" and s2 == "камень":
#     print("Тимур")
# elif s1 == "камень" and s2 == "ящерица":
#     print("Тимур")
# elif s1 == "ящерица" and s2 == "Спок":
#     print("Тимур")
# elif s1 == "Спок" and s2 == "ножницы":
#     print("Тимур")
# elif s1 == "ножницы" and s2 == "ящерица":
#     print("Тимур")
# elif s1 == "ящерица" and s2 == "бумага":
#     print("Тимур")
# elif s1 == "Спок" and s2 == "камень":
#     print("Тимур")

# else:
#     print("Руслан")

# s = input().split("О")
# print(len(max(s)))
# print(s)


# for i in range(int(input())):
#     s = input().lower()
#     if ("a" in s) and ("n" in s) and ("t" in s) and ("o" in s):
#         if s.count("n")>=2:
#             a = s.find("a")
#             n1 = s.find("n", a+1, len(s) )
#             t = s.find("t", n1+1, len(s))
#             o = s.find("o", t+1, len(s))
#             n2 = s.find("n", o+1, len(s))
#             if (a<n1) and (n1<t) and (t<o) and (o<n2):
#                 print(i+1, end = " ")

            
word = input() + ' запретил букву '
alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range(len(alf)):
    if word[i] in alf:
        if len(word) > 1:
            print(word + alf[i])
            word = word.replace(alf[i],'')
            word = word.lstrip()
            word = word.replace("  "," ")
            #print(len(sword))
    
    
