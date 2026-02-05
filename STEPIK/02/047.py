# def matrix_mult(A, B):
#     # Умножение двух матриц A и B
#     return [[sum(x * y for x, y in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

# def matrix_power(matrix, n):
#     # Возведение матрицы в степень n
#     result = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
#     while n:
#         if n % 2 == 1:
#             result = matrix_mult(result, matrix)
#         matrix = matrix_mult(matrix, matrix)
#         n //= 2
#     return result

# # Определяем матрицу
# a = [[1, 0],
#      [4, 1]]

# # Возводим матрицу в 25-ю степень
# result = matrix_power(a, 25)

# # Выводим результат
# for row in result:
#     print(row)

s = input().split()
n, m = int(s[0]), int(s[1])
m1,m2 = [],[]
for i in range(n):
    temp = [int(num) for num in input().split()]
    m1.append(temp)
a = input()    
i = 0
for i in range(n):
    temp = [int(nu) for nu in input().split()]
    m2.append(temp)
i = 0
m3 = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range (m):
        m3[i][j] = m1[i][j]+m2[i][j]

for r in range(n):
    for с in range(m):
        print(m3[r][с], end=' ')
    print()