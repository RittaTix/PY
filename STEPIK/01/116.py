# numbers = [8, 9, 10, 11]
# numbers[2] = 17
# numbers += [4, 5, 6]
# del numbers[0]
# numbers = numbers*2
# numbers.insert(3,25)
# print(numbers)

# s = input().split()
# for i in range(len(s)):
#     s[i] = int(s[i])
# ind_min = s.index(min(s))
# ind_max = s.index(max(s))
# s[ind_min], s[ind_max] = s[ind_max], s[ind_min]
# for i in range(len(s)):
#     s[i] = str(s[i])
# print(" ".join(s))

# text = input().lower().split()

# a1 = text.count("an")
# a2 = text.count("a")
# a3 = text.count("the")

# print("Общее количество артиклей:",a1+a2+a3)

# s = input()
# n = int(s[1:])
# for i in range(n):
#     stk = input()
#     if "#" in stk:
#        stk_n = stk[:stk.find("#")] 
#        print(stk_n.rstrip())
#     else:
#         print(stk)

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)

# print(numbers)

# sp = input().split()
# for i in range(len(sp)):
#     sp[i] = int(sp[i])
# a = sorted(sp)
# b = sorted(sp,reverse=True)
# print(*a)
# print(*b)


n = int(input())
sp = []
for i in range(n):
    sp.append(input())
print(*sorted(sp), sep = "\n")