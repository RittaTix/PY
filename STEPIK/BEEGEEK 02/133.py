# a,b = complex(input()),complex(input())
# print(f'{a} + {b} = {a+b}')
# print(f'{a} - {b} = {a-b}')
# print(f'{a} * {b} = {a*b}')



# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# numbers_mod = [abs(i) for i in numbers]
# isk =  numbers_mod.index(max(numbers_mod))
# print(numbers[isk])
# print(numbers_mod[isk])

n, z1, z2 = int(input()), complex(input()), complex(input())

print(z1**n + z2**n + (z1.conjugate())**n + (z2.conjugate())**(n+1))
