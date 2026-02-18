# n,m = int(input()), int(input())
# mult = [[0]*m for _ in range(n)]
# mult = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]
# for r in range(n):                    # выводим матрицу
#     for c in range(m):
#         print(mult[r][c], end=' ')
#     print()


# n,m = int(input()), int(input())
# matrix = []
# for i in range(n):
#      temp = [int(num) for num in input().split()]
#      matrix.append(temp)
# r_max = 0
# c_max = 0
# zn_max = int(matrix[0][0])
# for r in range(n):                   
#     for c in range(m):
#          if int(matrix[r][c])>zn_max:
#             zn_max = int(matrix[r][c])
#             r_max = r
#             c_max = c      
# print(r_max, c_max)


# n, m = int(input()), int(input())
# matrix = []
# for i in range(n):
#      temp = [int(num) for num in input().split()]
#      matrix.append(temp)

# s = input().split()
# i = int(s[0])
# j = int(s[1])

# for r in range(n):                   
#     for c in range(m):
#          if c == i:
#               (matrix[r][c]), (matrix[r][j]) = (matrix[r][j]), (matrix[r][c])
                  
# for r in range(n):                    # выводим матрицу
#     for c in range(m):
#         print(matrix[r][c], end=' ')
#     print()


# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# pr = "YES"
# for r in range(n):                   
#     for c in range(n):
#         if matrix[r][c] != matrix[c][r]:
#             pr = "NO"
#             break
# print(pr)

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# for r in range(n):                   
#     for c in range(n):
#          if r == c:
#            matrix[r][c], matrix[n-r-1][r] = matrix[n-r-1][r],matrix[r][c]

# for r in range(n):                    # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# matrix.reverse()

# for r in range(n):                    # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# matrix.reverse()

# for r in range(n):                    # выводим матрицу
#     for c in range(n):
#         print(matrix[c][r], end=' ')
#     print()


# start = input()
# matrix = [['.' for _ in range(8)] for _ in range(8)]  # b6
# pos_x, pos_y = 8-int(start[1]), ord(start[0])-97
# matrix[pos_x][pos_y] = 'N'

# for r in range(8):                    # выводим матрицу
#     for c in range(8):
#         #INX = (int(p[0]) - r-1) * (int(p[1]) - c-1)
#         INX = (pos_y - c) * (pos_x - r) 
#         if INX in [-2, 2]:
#             print("*", end=' ')    
#         else:
#             print(matrix[r][c], end=' ')
#     print()

n = int(input())  
flag = "YES"

matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

sum_e = 0
pe_st = matrix[0] #сумма первой строки
for d in range(n):
    sum_e += int(pe_st[d])

sp = list(range(1,n**2+1)) #проверяю наличие всех цифр
for r in range(n):
    for c in range(n):
        try:
            sp.pop(sp.index(matrix[r][c]))
        except ValueError:
            flag = "NO"
            break

if flag == "YES":    # проверяю сумму строк

    sum_s = 0
    for k in range(n):
        my_list = matrix[k]
        for l in range(n):
            sum_s += int(my_list[l])  
        if sum_e == sum_s:
            flag = "YES"
        else:
            flag = "NO" 
            break    
        sum_s = 0    

if flag == "YES": #проверяю сумму колонок
    z = 0
    sum_k=0
    while z<(n+1):
        for u in range(n): 
            sum_k += int(matrix[u][z])
        if sum_e == sum_k:
            flag = "YES"
        else:
            flag = "NO" 
            break    
        sum_k = 0 
        z+=1

r = 0
с = 0
if flag == "YES": # проверяю диагонали
    pr_dia_g = 0
    pr_dia_p = 0
    for r in range(n):
        for c in range(n):
            if r == c:
                pr_dia_g += int(matrix[r][c])
            if (r + c +1) == n:
                pr_dia_p += int(matrix[r][c])
    if  pr_dia_g == pr_dia_p:
        flag = "YES"
    else:
        flag = "NO"

print(flag)



