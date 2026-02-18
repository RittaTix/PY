# zeros = [0] * 10
# print(len(zeros))

# numbers = [10, 20, 30, 40, 50]
# print(numbers[-2])
# print(numbers[-4:-1])

# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# print(numbers[2:5])
# print(numbers[:4])
# print(numbers[3:])

# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# print(numbers[2:5])
# print(numbers[:4])
# print(numbers[3:])

# numbers = [4, 8, 12, 16, 34, 56, 100]
# numbers[1:4] = [20, 24, 28]
# print(numbers)

# numbers = [5, 10, 15, 25]
# print(numbers[::-2])

# numbers = [10, 20, 30, 40]
# del numbers[0:6]
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# new_numbers = [2 * x for x in numbers]
# print(new_numbers)

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)

# print(list1)


# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)

# list2 = []
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in range(len(list1)):
#     list2 += list1[i]
# maximum = max(list2) 

# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

# list1 = [i.reverse() for i in list1]
# print(list1)

# a = [[1, 2, 3], [4, 5, 6]]
# print(a.reverse())


# a = [[1, 2, 3], [4, 5, 6]]
# b = [i.reverse() for i in a]
# print(b)


# a = [[1, 2, 3], [4, 5, 6]]
# for i in a:
#     i.reverse()
# print(a)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
# print(list1)

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for i in list1:
    total += sum(i)
    counter += len(i)
print(total/counter)