# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# s = input()
# words = s.split()
# print(*words, sep = "\n")

# s = input()
# words = s.split()
# for i in range(len(words)):
#     p = words[i]
#     print(p[0], end = ". ")

# s = input()
# words = s.split('\\')
# print(*words, sep = "\n")

# s = input()
# words = s.split('.')
# count = 0
# for i in range(len(words)):
#     if int(words[i]) >= 0 and int(words[i]) < 255:
#         count+=1
# if count == 4:
#     print("ДА")
# else:
#     print("НЕТ")

# s = input()
# r = input()
# print(r.join(s))


# s = input().split()
# count = 0
# for i in range(len(s)):
#     for j in range (i+1,len(s)):
#         if s[i] == s[j]:
#             count += 1
# print(count)

colors = ['Orange']
colors.append('Red')
colors.append('Blue')
colors.append('Green')
colors.insert(0, 'Violet')
colors.insert(2, 'Purple')

print(colors)

 
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
del colors[-1]
colors.remove('Green')

print(colors)