
# s = input().split()
# n, m = int(s[0]), int(s[1])
# lst = [([i for i in ('.' * int(m))]) for i in range(int(n))]

# for i in range(n):
#     for j in range(m):
#         if j % 2 == 1 and i % 2 == 0:
#             lst[i][j] = '*'
#         if j % 2 == 0 and i % 2 == 1:
#             lst[i][j] = '*'
# for r in range(n):                    # выводим матрицу
#     for c in range(m):
#         print(lst[r][c], end=' ')
#     print()

# n = int(input())
# matrix = [[0]*n for _ in range(n)]
# for _ in range(n):                   
#     matrix[_][n-_-1] = 1
 
# for i in range(n):
#     for j in range(n):
#         if i +j >= n:
#             matrix[i][j] = 2 

# for r in range(n):                    # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()


# n,m = input().split()
# n,m = int(n), int(m)
# matrix = [[0]*m for _ in range(n)]
# z = 1
# for i in range (n):
#     for j in range (m):
#         matrix[i][j] += z
#         z +=1
#     print()

# for r in range(n):                    # выводим матрицу
#     for c in range(m):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()


# n,m = input().split()
# n,m = int(n), int(m)
# matrix = [[0]*m for _ in range(n)]
# z = 1
# for i in range (m):
#     for j in range (n):
#         matrix[j][i] += z
#         z +=1
#     print()

# for c in range(n):                    # выводим матрицу
#     for r in range(m):
#         print(str(matrix[c][r]).ljust(3), end=' ')
#     print()


# n = int(input())
# matrix = [[0]*n for _ in range(n)]

# for i in range(n):                    # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 1

# for k in range(n):
#     for l in range(n):
#         if (k < l) and (k < (n-1-l)):
#             matrix[k][l] = 1

# for k in range(n):
#     for l in range(n):
#         if (k > l) and (k > (n-1-l)):
#             matrix[k][l] = 1

# for r in range(n):                    # выводим матрицу
#     for c in range(n):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()


#

# n,m = input().split()
# n,m = int(n), int(m)
# matrix = [[0]*m for _ in range(n)]
# z = 0
# for i in range(n):
#     #z = i+1
#     for j in range(m):
#         matrix[i][j] =  (i  + j) % m + 1
#         #z += 1

# for r in range(n):                    # выводим матрицу
#     for c in range(m):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()

# n,m = input().split()
# n,m = int(n), int(m)
# matrix = [[0]*m for _ in range(n)]
# z = 1
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] +=z
#         z += 1

# for k in range(1,n,2):
#     matrix[k].reverse()

# for r in range(n):                    # выводим матрицу
#     for c in range(m):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()



# n,m = input().split()
# n,m = int(n), int(m)
# matrix = [[0]*m for _ in range(n)]
# buka = 1

# for i in range(n+m):
#     for j in range(n):
#         for k in range(m):
#             if (j+k) == i:
#                 matrix[j][k] = buka
#                 buka += 1
# for r in range(n):                    # выводим матрицу
#     for c in range(m):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()

n,m = input().split()
n,m = int(n), int(m)
matrix = [[0]*m for _ in range(n)]

i, j = 0, 0
di, dj = 0, 1
for k in range(n*m):
    matrix

def spiral_fill(n, m):
    matrix = [[0]*m for _ in range(n)]
    num = 1
    top, bottom = 0, n-1
    left, right = 0, m-1

    while left <= right and top <= bottom:
        # Заполняем верхнюю строку слева направо
        for j in range(left, right+1):
            matrix[top][j] = num
            num += 1
        top += 1

        # Заполняем правый столбец сверху вниз
        for i in range(top, bottom+1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            # Заполняем нижнюю строку справа налево
            for j in range(right, left-1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1

        if left <= right:
            # Заполняем левый столбец снизу вверх
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


# Чтение входных данных
n, m = map(int, input().split())
result = spiral_fill(n, m)

# Вывод результата
for row in result:
    print(' '.join(f'{x:2d}' for x in row))