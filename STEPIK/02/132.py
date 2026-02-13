# from fractions import Fraction

# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']


# for i in numbers:
#     print(i, "=", Fraction(i))


# from fractions import Fraction

# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

# sp = [Fraction(i) for i in s.split()]

# print(min(sp) + max(sp))


# from fractions import Fraction

# print(Fraction(int(input()),int(input())))

# from fractions import Fraction

# n,m = input(), input()

# print(n,'+',m, '=', Fraction(n) + Fraction(m))
# print(n,'-',m, '=', Fraction(n) - Fraction(m))
# print(n,'*',m, '=', Fraction(n) * Fraction(m))
# print(n,'/',m, '=', Fraction(n) / Fraction(m))

# 2/3 + 3/7 = 23/21
# 2/3 - 3/7 = 5/21
# 2/3 * 3/7 = 2/7
# 2/3 / 3/7 = 14/9


# from fractions import Fraction
# n = int(input())
# z = Fraction(0)
# for i in range(1,n+1):
#     z += Fraction(1,i**2) 

# print(z)

# from fractions import Fraction
# from math import factorial
# n = int(input())
# z = Fraction(0)
# for i in range(1,n+1):
#     z += Fraction(1,factorial(i)) 

# print(z)

# from fractions import Fraction
# from math import *
# n = int(input())
# sp = []
# for i in range(1,ceil(n/2)):
#     if (Fraction(i,n-i)).numerator + (Fraction(i,n-i)).denominator == n:
#         sp.append(Fraction(i,n-i))
# print(max(sp))


# from fractions import Fraction
# n = int(input())
# sp = []

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         sp.append(Fraction(j,i))

# print(*sp, sep='\n')

# Два for, в первом i от 1 до n + 1, во втором j от i до n +1(это чтобы лишний раз программу за ненадобностью не гонять).  
# Потом условие if gcd(наши числа на данной итерации i, j) равны 1: Дальше через Fraction(i, j)  добавляем в пустой list. 
# В конце выводим его через sorted

from fractions import Fraction
from math import gcd
n = int(input())
sp = []

for i in range(1,n+1):
    for j in range(i + 1, n + 1):
        if gcd (i,j) == 1:
            sp.append(Fraction(i,j))

print(*sorted(sp), sep='\n')