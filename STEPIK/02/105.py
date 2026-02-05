# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

# result = { v:k for k,v in months.items()}
# print(result)

# numbers = [-3, 6, 4, 76, 2, -1, 2]
# dict = {i:numbers[i]**2 for i in range(len(numbers))}
# print(dict)

# colors = {'a1': 'Blue', 'b2': 'Orange', 'b4': None, 'a6': 'Red', 'c4': None}
# result = {i:colors[i] for i in colors if colors[i] is not None}
# print(result)

# favorite_numbers = {
#     'scarlett': 41, 'den': 22, 'viktor': 321, 'lera': 777, 'mahad': 4,
#     'manny': 4, 'ken': 8423, 'borya': 12
# }

# result = {i: favorite_numbers[i] for i in favorite_numbers if len(str(favorite_numbers[i])) == 2}
# print(result)

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

# dict = {int((i.split(":")[0])):(i.split(":")[1]) for i in s.split(" ")}

# print(dict)
# # print(s.split(" "))
# # print(type(s.split(" ")))

# numbers = [1, 6, 18]

# dict = {i:[z+1 for z in range(i) if i % (z+1) == 0] for i in numbers}

# print(dict)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# dict = {i:[ord(z) for z in i] for i in words}
# print(dict)

# from pprint import pprint
# pprint(dict)


# letters = {4: 'К', 65: 'Щ', 12: 'П', 41: 'М', 36: 'У'}
# remove_keys = [12, 65, 14, 37]

# dict = {k: letters[k] for k in letters if k not in remove_keys}
# print(dict)

# students = {'Сергей': (165, 62), 'Дима': (178, 61), 'Катя': (162, 62), 'Диана': (168, 69)}
# dict = {i: students[i] for i in students if (students[i][0] > 167 and students[i][1] < 75)}
# print(dict)