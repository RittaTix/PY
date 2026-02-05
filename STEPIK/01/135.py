# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     return side1+side2>side3 and side1+side3>side2 and side2+side3>side1

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))

# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, num // 2 + 1):
#         if num % i == 0: 
#             return False
#     return True
# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))


# #объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, num // 2 + 1):
#         if num % i == 0: 
#             return False
#     return True


# #объявление функции
# def get_next_prime(num):
#     while is_prime(num+1) != "True":
#         if is_prime(num+1)== True:
#             return num+1
#         else:
#             num += 1

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))

# # объявление функции
# def is_password_good(password):
#     if len(password)<8:
#         return False
#     ZS_p = False
#     SS_p = False
#     ZI_p = False
#     for i in range(len(password)):
#         if password[i].isupper():
#              ZS_p = True

#         if password[i].islower():
#              SS_p = True
        
#         if password[i].isdigit():
#              ZI_p = True

#     return ZS_p and SS_p and ZI_p       

       
# # считываем данные
# txt = input()

# # вызываем функцию
#print(is_password_good(txt))



# # объявление функции
# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     for i in range (len(word1)):
#         if word1[i] != word2[i]:
#             count+=1
#     if count == 1:
#         return True
#     else:
#         return False
    
# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))


# # объявление функции
# def is_palindrome(text):
#     text = text.lower()
#     text = text.replace(" ", "")
#     text = text.replace(",", "")
#     text = text.replace(".", "")
#     text = text.replace("!", "")
#     text = text.replace("?", "")
#     text = text.replace("-", "")
#     return text == text[::-1]
 
# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_palindrome(txt))


# # объявление функции
# def is_valid_password(password):
#     if password.count(':')>2:
#         return False
#     sp = password.split(":")
#     if sp[0] != sp[0][::-1]:
#         return False
    
#     if int(sp[1]) == 1:
#        return False 
    
#     if int(sp[1]) > 1:
#         for i in range(2, int(sp[1]) // 2 + 1):
#             if int(sp[1]) % i == 0:
#                 return False
    
#     if int(sp[2]) % 2 != 0:
#         return False

#     return True  
  
# # считываем данные
# psw = input()

# # вызываем функцию
# print(is_valid_password(psw))

# # объявление функции
# def is_correct_bracket(text):
#     count = 0
#     for i in range(len(text)):
#         if text[i] == "(":
#             count += 1
#         else:
#             count -= 1
#             if count < 0:
#                 return False
#     return count == 0
        

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_correct_bracket(txt))

# # объявление функции
# def convert_to_python_case(text):
#     str_it = (text[0]).lower()
#     for i in range(1,(len(text))):
#         if text[i].isupper():
#             str_it += "_"
#             str_it += (text[i]).lower()
#         else:
#             str_it += text[i]
#     return str_it
# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))

