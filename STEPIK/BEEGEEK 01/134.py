# # объявление функции
# def convert_to_miles(km):
#     return km * 0.6214

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(convert_to_miles(num))



# # объявление функции
# def get_days(month):
#     sp = [31,28,31,30,31,30,31,31,30,31,30,31]
#     return sp[month-1]
# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))


# # объявление функции
# def get_factors(num):
#     sp = []
#     for i in range (num + 1):
#         if num % (i+1) == 0:
#             sp.append(i+1)
#     return sp
# # считываем данные
# n = int(input())

# # вызываем функцию
# get_factors(n)

# # объявление функции
# def number_of_factors(num):
#     return len(get_factors(num))

# # вызываем функцию
# print(number_of_factors(n))


# # объявление функции
# def find_all(target, symbol):
#     sp =[]
#     for i in range(len(target)):
#         if target[i] == symbol:
#             sp.append(i)
#     return sp
# # считываем данные
# s = input()
# char = input()

# # вызываем функцию
# print(find_all(s, char))


# # объявление функции
# def merge(list1, list2):
#     list3 = list1 + list2
#     return sorted(my_list)

# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))

# def quick_merge(sp):
#     for j in range(len(sp)):
#         sp[j] = int(sp[j])
#     return sorted(sp)

# n = int(input())
# sp2 = []
# for i in range(n):
#     sp1 = input().split()                            
#     sp2 += sp1                                         

# print(*quick_merge(sp2))


# # объявление функции
# def code_format(text):
#     text = "<code>" + text + "</code>"
#     return text

# # считываем данные
# text = input()

# # вызываем функцию
# print(code_format(text))

# print(int(9.56+0.5))
# print(int(14.489+0.5))
# print(int(6.5+0.5))
# print(int(0.49+0.5))
# print(int(8.51+0.5))
# print(int(5.5+0.5))
# print(int(2+0.5))
# print(int(8.499999999+0.5))
# print(int(13.49999999+0.5))
# print(int(8.5+0.5))


# # объявление функции
# def math_round_to_int(num):
#     num = int((num + 0.5))
#     return num
# # считываем данные
# num = float(input())

# # вызываем функцию
# print(math_round_to_int(num))

# # объявление функции
# def get_unique(numbers):
#     sp = []
#     for i in numbers:
#         if i not in sp:
#             sp.append(i)
#     return sp
# # считываем данные
# numbers = eval(input())

# # вызываем функцию
# print(get_unique(numbers))

# объявление функции
def get_last_index(data, value):
    sp = data[-1::-1]
    for i in range(len(sp)):
        if sp[i] == value:
            i = len(sp) -i -1
            break
        else:
            i ="ERROR!"
    return i
# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))