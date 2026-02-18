# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if numbers.count("5")>0 and numbers.count("17")>0:
#     print("YES")
# else:
#     print("NO")
# del numbers[-1]
# del numbers[0]
# print (numbers)

#import this

# n = int(input())
# sp = []
# for i in range(n):
#     l = int(input())
#     sp.append(l**3)
# print(sp)

# n = int(input())
# sp = [1]
# for i in range(2,n//2+1):
#     if n%i == 0:
#         sp.append(i)
# sp.append(n)
# print(sp)

# n = int(input())
# sp =[]
# a = int(input())
# for i in range(n-1):
#     b = int(input())
#     sp.append(a+b) 
#     a = b
# print(sp)    

# n = int(input())
# sp = []
# for i in range(n):
#     a = int(input())
#     sp.append(a)
# del sp[1::2]
# print(sp)

# n = int(input())
# sp = []
# spb = ""
# for i in range(n):
#     a = input()
#     sp.append(a)
# k = int(input())

# for j in range(len(sp)):
#     w = sp[j]
#     if len(w) < k-1:
#         continue
#     l = w[k-1]
#     spb += l

# print(spb)

n = int(input())
str=[]
for i in range(n):
    s = input()
    for j in range(len(s)):
        str.extend(s[j])
print(str)