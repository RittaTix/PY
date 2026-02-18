# sp = input().split()
# n = int(input())
# sp2 = []
# z = 0
# for i in range(len(sp)//n):
#     sp2.append(sp[z:(z+n)])
#     z+=n

# print(*sp2)


# sp1 = input().split()
# n = int(input())
# sp2 = []

# for i in range(n):
#     sp2.append(sp1[i::n])

# print(sp2)


# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# i = 0
# sp = []

# for i in range(n):
#     for j in range(n):
#         if (((i<=j) and (i>=(n-1-j))) or ((i>=j) and (i>=(n-1-j)))):
#             sp.append(matrix[i][j])
# print(max(sp))

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for r in range(n):
#     for с in range(n):
#         print(matrix[с][r], end =' ')
#     print()

# n = int(input())
# matrix = [["."]*n for _ in range(n)]

# for _ in range(n):  # заполняем главную и побочную диагонали                 
#     matrix[_][n-_-1] = "*"
#     matrix[_][_] = "*"

# for i in range(n): #заполняем вертикаль и горизонталь
#      for j in range(n):
#         if i == n//2:
#              matrix[i][j] = "*" 
#         if j == n//2:
#              matrix[i][j] = "*" 

# for r in range(n):                    # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()




# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# flag = "YES"
# for i in range(n):
#        for j in range(n):
#             if matrix[i][j] != matrix[n-j-1][n-i-1]:
#                  flag = "NO"
#                  break
# print(flag)



# n = int(input())
# matrix1, matrix2= [], []
# z = 0
# for i in range(n):
#     temp = [int(nu) for nu in input().split()]
#     matrix1.append(temp)

# matrix_2 = [[matrix1[l][k] for k in range(n)] for l in range(n)],

# for i in range(n):
#     for j in range(n+1):
#         if j in matrix1[i] and j in matrix2[i]:
#             z += 1
# if n*n == z:
#     print("YES")
# else:
#     print("NO")


# put your python code here
start = input()
matrix = [['.' for _ in range(8)] for _ in range(8)]  # b6
pos_x, pos_y = 8-int(start[1]), ord(start[0])-97
matrix[pos_x][pos_y] = 'Q'

for r in range(8):                    # выводим матрицу
    for c in range(8):
        if (r == pos_x) and (c == pos_y):
            print("Q", end=' ') 
        elif abs(pos_x - r) == abs(pos_y - c) or pos_x == r or pos_y == c:
            print("*", end=' ')
        else:
            print(matrix[r][c], end=' ')
    print()