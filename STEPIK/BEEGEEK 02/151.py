# def fancy(length, char1, char2):
#     return (char1 + char2) * length + char1


# print(fancy(5, '-', '*'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(3))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(3, '.'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(2, ':', '|'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(4, char2='#'))


# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(char2='$', length=3))

# sp = []
# def matrix(n=1,m=None,value=0,):
#     if n == 1 and m == None:
#         m = 1
#         sp.append[0]
#     elif 
#     return sp

def matrix(n=1, m=None, value=0):
    sp = []
    if m == None:
        m = n
        sp = [[value]*n for _ in range(m)]
    elif n>=1 and m>=1:
        sp = [[value]*m for _ in range(n)]
    return sp

# print(matrix())         # матрица 1 × 1 из 0
# print(matrix(3))        # матрица 3 × 3 из 0
print(matrix(3, 1))     # матрица 3 × 1 из 0
# print(matrix(2, 5))     # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))  # матрица 3 × 4 из 9