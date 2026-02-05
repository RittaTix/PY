# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

# maximum = my_list[0][0]
# minimum = my_list[0][0]

# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)

# print(maximum + minimum)

# n = int(input()) 
# my_list = []
# for i in range(n):
#     my_list.append(i+1)
# for i in range(n):
#     print(my_list)

# n = int(input()) 
# my_list = []
# v = 1
# for i in range(n):
#     my_list.append(v)
#     v+=1
#     print(my_list)

# n = int(input())
# result = []

# for i in range(1, n + 1):
#     result.append(list(range(1, i + 1)))

# print(*result, sep='\n')
    
# import math
# n = int(input())
# result = []
# for i in range(1,n+1):
#     list2 = []
#     for j in range(1,i+1):
#         list2.append(int(math.factorial(n)/(math.factorial(j)*math.factorial(n-j))))
#     print(list2)    

# import math
# n = int(input())
# for i in range(0,n):
#     list2 = []
#     for j in range(0,n):


# import math
# n = int(input())
# for i in range(n):
#     print(*math.pascal(i))

# def PrintPasTriangle(rows):
#     row = [1]
#     for i in range(rows):
#         print(*row, sep=' ')
#         row = [sum(x) for x in zip([0]+row, row+[0])]
# n = int(input())        
# PrintPasTriangle(n)

# char_list = []
# a = []
# for char in input().split():
#     if not a:
#         a.append(char)
#     else:
#         if a[-1] == char:
#             a.append(char)
#         else:
#             char_list.append(a)
#             a = []
#             a.append(char)
# if a:
#     char_list.append(a)
# print(char_list)


# def chunked(sp2,n):
#     sp1 = []
#     for i in range(0,len(sp2),n):
#         sp1.append(sp2[i:i+n])
#     print(sp1)

# sp2 = input().split()
# n = int(input())

# chunked(sp2,n)

n = input().split()
fin, tot = [], []
for i in range(0, len(n)):
    for j in range(0, len(n)):
        fin = n[j:i + j + 1]
        if len(fin) == i + 1:
            tot.append(fin)
print([[]]+tot[::1])