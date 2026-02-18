# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()

n = 5
a = [[19, 21, 33, 78, 99], 
     [41, 53, 66, 98, 76], 
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

# maximum = -1
# minimum = 100

# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]

# print(minimum + maximum)

# n, m = int(input()), int(input())
# a = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range (m):
#         a[i][j] = input()

# for row in a:            
#     for elem in row:    
#         print(elem, end = ' ')
#     print()

# put your python code here



# n, m = int(input()), int(input())
# a = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range (m):
#         a[i][j] = input()

# for row in a:            
#     for elem in row:    
#         print(elem, end = ' ')
#     print()

# print()

# for i in range(m):
#     for j in range(n):
#         print(a[j][i], end=' ')
#     print()

# n = int(input())
# total = 0
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             total += matrix[i][j]
# print(total)


# n = int(input())
# total = 0
# matrix = []
# count = 0
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         total += matrix[i][j]
#     for k in range(n):
#         if matrix[i][k] > total/n:
#             count +=1
#     print(count)
#     total = 0
#     count = 0

# n = int(input())
# matrix = []
# sp1 = []
# for i in range(n):
#      temp = [int(num) for num in input().split()]
#      matrix.append(temp)
# for i in range(n):
#      for j in range(n):
#           if ((i>=j) and (i<=(n-1-j))):
#                sp1.append (int((matrix[i][j])))
# for i in range(n):
#      for j in range(n):
#           if ((i<=j) and (i>=(n-1-j))):
#                sp1.append (int((matrix[i][j])))

# print(max(sp1)) 


n = int(input())
matrix = []
for i in range(n):
     temp = [int(num) for num in input().split()]
     matrix.append(temp)
sum_up = 0
sum_down = 0
sum_right = 0
sum_left = 0
for i in range(n):
     for j in range(n):
        if (i<j and i+j+1<n):
               sum_up += matrix[i][j]
        if (i>j and i+j+1>n):
               sum_down += matrix[i][j]
        if (i<j and i+j+1>n):
               sum_right += matrix[i][j]
        if (i>j and i+j+1<n):
               sum_left += matrix[i][j]

print("Верхняя четверть:", sum_up)
print("Правая четверть:", sum_right)
print("Нижняя четверть:", sum_down)
print("Левая четверть:", sum_left)

                