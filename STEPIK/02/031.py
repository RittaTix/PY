# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1) 
# print(res)


# объявление функции
def func(num1, num2):
    return num1%num2 == 0
# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print("делится")
else:
    print("не делится")