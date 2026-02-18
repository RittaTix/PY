# # объявление функции
# def print_digit_sum(num):
#     s = 0
#     while num != 0:  # пока в числе есть цифры
#         last_digit = num % 10  # получить последнюю цифру
#         num = num // 10  # удалить последнюю цифру из числа
#         s += last_digit
#     print(s)    
# # считываем данные
# n = int(input())

# # вызываем функцию
# print_digit_sum(n)

     



# # объявление функции
# def print_case_counts(s):
#     U, L = 0, 0
#     for i in s:
#         if i.isalpha():
#             if i.isupper():
#                 U += 1
#             else:
#                 L += 1
#     print("Букв в верхнем регистре:",U)
#     print("Букв в нижнем регистре:",L)
# # считываем данные
# s = input()

# # вызываем функцию
# print_case_counts(s)


# # объявление функции
# def print_sorted_hyphen(s):
#     s1 = sorted(s.split("-"))
#     print("-".join(s1))
# # считываем данные
# s = input()

# # вызываем функцию
# print_sorted_hyphen(s)

# # объявление функции
# def print_perm_time_call(msc_time):
#     msc_h, msc_m = int(msc_time[0:2]),int(msc_time[3:])   
#     perm_time = msc_h*60 + msc_m + 120
#     perm_h = perm_time // 60
#     if len(str(perm_h))<2:
#         perm_h = "0" + str(perm_h)
#     perm_m = perm_time - perm_time // 60 * 60
#     if len(str(perm_m))<2:
#         perm_m = "0" + str(perm_m)

#     print("Созвон будет в ",perm_h , ":",perm_m , ".", sep='')

# # считываем данные
# msc_time = input()

# # вызываем функцию
# print_perm_time_call(msc_time)


# объявление функции
def print_symbol_counts(s):
    s1 = s.lower()
    sp = []
    for symbol in s1:
        if symbol not in sp:
            sp.append(symbol)

    for i in sorted(sp):
        print(i, ": ", s1.count(i), sep="")
# считываем данные
s = input()

# вызываем функцию
print_symbol_counts(s)