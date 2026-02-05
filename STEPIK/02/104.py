# dict = {}
# for i in range(int(input())):
#     key, value = input().split(': ')
#     dict.setdefault(key.lower(),value)

# for j in range(int(input())):
#     j = input().lower()
#     print(dict.get(j,"Не найдено"))

# i, j = input(), input()

# dict1, dict2 = {}, {}
# for s1 in i:
#     dict1[s1] =  dict1.get(s1,0)+1
# for s2 in j:
#     dict2[s2] =  dict2.get(s2,0)+1
# if dict1 == dict2:
#     print("YES")
# else:
#     print("NO")



# str1 = [el.lower() for el in input() if el.isalpha()] 
# str2 = [el.lower() for el in input() if el.isalpha()] 

# dict1, dict2 = {}, {}
# for s1 in str1:
#     dict1[s1] =  dict1.get(s1,0)+1
# for s2 in str2:
#     dict2[s2] =  dict2.get(s2,0)+1
# if dict1 == dict2:
#     print("YES")
# else:
#     print("NO")



# def s(word):
#     res = {}
#     for i in word.lower():
#         if i.isalpha():
#             res[i] = res.get(i, 0) + 1
#     return res


# print(("NO", "YES")[s(input()) == s(input())])


# dict = {}
# for i in range(int(input())):
#     key, value = input().split()
#     dict.setdefault(key,value)

# zn = input()

# sinonim = dict.get(zn,"None")

# dict_inverted={}
# for k, v in dict.items():  
#    dict_inverted[v]=k

# if sinonim == "None":
#     sinonim = dict_inverted[zn]

# print(sinonim)

# dict = {}
# for i in range(int(input())):
#     sp = input().split()
#     dict[str(sp[0])] = sp[1:]

# for gg in range(int(input())):
#     gorod = input()
#     for k,v in dict.items():
#         for z in v:
#             if gorod == z:
#                 print(k)

# dict = {}
# for i in range(int(input())):
#     sp = input().split()
#     dict.setdefault(sp[1],[]).append(sp[0])

# for j in range(int(input())):
#     imya = str(input())

#     for k,v in dict.items():
#         if imya == k:
#             print(*v)
#         else:
#             print("абонент не найден")
            
            
# dict = {'Женя': ['79184219577', '79281234567'], 'Руслан': ['79194249271']}    
# # imya = "Женя"

# dict = {}
# for i in range(int(input())):
#     sp = input().split()
#     dict.setdefault(sp[1].lower(),[]).append(sp[0])

# for j in range(int(input())):
#     print(*dict.get(input().lower(),["абонент не найден"]))

str = '*!*!*?'
dict = {'3':'а', '2':'н','1':'с'}


# dict = {}
# str = input()
# for i in range(int(input())):
#     sp = input().split(": ")
#     dict.setdefault(sp[1],sp[0])
# print(dict)

# for z in str:
#     for key in dict:
#         if str.count(z) == int(key):
#             str = str.replace(z,dict[key])
# print(str)


dict_alpha = {}
shifr = input()
for i in range(int(input())):
    v, k = input().split(': ')
    dict_alpha[int(k)] = v
for i in shifr:
    print(dict_alpha[shifr.count(i)], end='')
    