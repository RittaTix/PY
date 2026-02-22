# listA = [2, 3, 4]
# listB = [3, 2, 1]

# result = sum(map(pow, listA, listB))
# print(result)

# from operator import mul
# from functools import reduce

# result = reduce(mul, range(1, 6))
# print(result)

# from operator import add

# result = list(map(add, 'abc', '1234'))
# print(result)


from operator import add
from functools import reduce

result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)