# numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
# print(min(numbers))
# print(max(numbers))

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# s = 0
# for i in numbers:
#     s+=(int(i))**2
# print(s)

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# fr_sorted = sorted(fruits)
# print(fr_sorted)

# s = input()
# if len(s) == len(set(s)):
#     print("YES")
# else:
#     print("NO")

# s = input()+input()
# if len(set(s)) == 10:
#     print("YES")
# else:
#     print("NO")

# s1, s2 = set(input()),set(input())
# if sorted(s1) == sorted(s2):
#     print("YES")
# else:
#     print("NO")

s = input().split()
if set(s[0])==set(s[1])==set(s[2]):
    print("YES")
else:
    print("NO")   