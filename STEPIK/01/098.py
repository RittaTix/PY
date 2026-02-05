# print(ord('a'), ord('A'))    
# print(ord('p'), ord('p'))    
# print(ord('x'), ord('y'))    
# print(ord('a'), ord('Z'))    
# print(ord('4'), ord('5'))    
# print(ord('9'), ord('0'))

# print(max("Generation","generation"))
# print(max("python","Python"))
# print(max("2024","2024"))
# print(max("GPT-3.5","GPT-4"))
# print(max("3.141592653589793","3.1416"))
# print(max("colour","color"))


#print(max('aunt', 'an', 'a', 'An'))

# s = input()
# mins = s
# maxs = s
# while s != 'КОНЕЦ':
#     mins = min(s,mins)
#     maxs = max(s,maxs)
#     s = input()
# print("Минимальная строка ⬇️:", mins)
# print("Максимальная строка ⬆️:", maxs)

# a = input()
# b = input()
# c = input()
# d = input()
# ms = min(a,b,c,d)
# bs = max(a,b,c,d)
# print((ord(ms[-1])*ord(bs[-1]))**2)

# n = int(input())
# for i in range(n):
#     s = input()
#     if len(s) < 3 and s[0] in '0123456789' and s[-1] in 'АБВГДЕЖЗИЙКЛМНОП':
#         print("YES")
#     else:
#         print("NO")

# s1 = input()
# s2 = input()

# ch_s1 = ""
# ch_s2 = ""


# for i in range (len(s1)):
#     if s1[i].isalpha(): 
#         ch_s1 += s1[i]
# for j in range (len(s2)):
#     if s2[j].isalpha(): 
#         ch_s2 += s2[j]

# if ch_s1.lower() == ch_s2.lower():
#     print("YES")
# else:
#     print("NO")


# a = input()
# b = input()
# c = input()

# s_min = min(a,b,c)
# s_max = max(a,b,c)
# s_avesome = (a+b+c)
# s_middle = s_avesome.replace(s_min,"")
# s_middle = s_middle.replace(s_max,"")
# print(s_min, s_middle, s_max)


# n = int(input())
# print(list(range(1,n+1)))


# n = int(input())
# s_old = input()
# s_old_f = (s_old[ : s_old.find(" ")])
# s_old_i = (s_old[s_old.find(",") : ])
# s_old_r = s_old_f + s_old_i
# flag = "YES"
# for i in range(n-1):
#     s_new = input()
#     s_new_f = (s_new[ : s_new.find(" ")])
#     s_new_i = (s_new[s_new.find(",") : ])
#     s_new_r = s_new_f + s_new_i
#     if s_old_r > s_new_r:
#         flag = "NO"
#         break
#     else:
#         flag = "YES"
#         s_old_r = s_new_r
# print(flag) 


# s = input()
# for i in range(len(s)):
#     if i%3 == 0:
#         continue
#     else:
#         print(s[i],end = "")

# s = input()
# print(s.replace("@",""))

# s = input()
# if "f" not in s:
#     print("-2")
# if s.count("f") == 1:
#     print("-1")
# if s.count("f") > 1:
#     s = s.replace("f","ы",1)
#     print(s.find("f"))

# s = input()
# a = s.find("h")
# b = s.rfind("h")
# print(s[:a]+s[b:a:-1]+s[b:])

# n = int(input())
# s = list("abcdefghijklmnopqrstuvwxyz")
# print(s[:n])

numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1+numbers1+numbers2*9+numbers3)