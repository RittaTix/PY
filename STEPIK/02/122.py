# from random import randint
# def generate_ip():
#     return (str(randint(1,255)) + "."+ str(randint(1,255)) + "." + str(randint(1,255)) + "." + str(randint(1,255)))

# print(generate_ip())

# from random import randrange as r

# def generate_index():
#     return f'{chr(r(65,90))}{chr(r(65,90))}{r(90)}_{r(90)}{chr(r(65,90))}{chr(r(65,90))}'

#     #LetterLetterNumber_NumberLetterLetter

# print(generate_index())

# from random import shuffle 
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
        
# for i in matrix:
#     shuffle(i)

# print (matrix)

# import random
# for i in range(100):
#     print(random.randint(1000000,9999999))

# from random import shuffle
# word = list(input())
# shuffle(word)
# print(''.join(word))

# import random
# numbers = random.sample(range(1,76), 25)
# numbers[12] = 0
# for i in range(25):
#     print(numbers[i],end=" ")
#     if (i + 1) % 5 == 0:
#         print()

# from random import sample

# numbers = sample(list(range(1, 76)), 25)
# bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
# bingo[2][2] = 0

# for i in range(5):
#     for j in range(5):
#         print(str(bingo[i][j]).ljust(3), end=' ')
#     print()


# from random import shuffle, sample
# sp = ['Владимир Смолов', 'Тагир Хан', 'Давид Лавров', 'Арина Приходько', 'Глеб Анисимов']
# p = sample(range(len(sp)),len(sp))
# sp_shuffle = []
# for j in p:
#     sp_shuffle.append(sp[j])

# for i in range(len(sp)):
#     print(sp[i], sp_shuffle[i])

# import random
# sp = [input() for y in range(int(input()))]
# items = sp[:]
# i = len(items)
# while i > 1:
#     i = i - 1
#     j = random.randrange(i)  # 0 <= j <= i-1
#     items[j], items[i] = items[i], items[j]

# for z in range(len(sp)):
#     print(sp[z], "-", items[z])

# from string import *
# import random


# LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

# def generate_password(length):
#     return random.sample(LETTER,length)


# def generate_passwords(count, length):
#     for i in range(count):
#         print("".join((generate_password(length))))

# n, m = int(input()), int(input())

# generate_passwords(n,m)

# from string import *
# import random

# LETTER = {'EN': [x for x in ascii_uppercase if x not in 'OI'],
#           'en': [x for x in ascii_lowercase if x not in 'ol'],
#           'dig': [x for x in digits if x not in '01']}

# def generate_password(length):
#     pass

# def generate_passwords(count, length):
#     pass

# n, m = int(input()), int(input())


# from string import *
# import random
# lenght = 8
# LETTER = {'EN': [x for x in ascii_uppercase if x not in 'OI'],
#           'en': [x for x in ascii_lowercase if x not in 'ol'],
#           'dig': [x for x in digits if x not in '01']}

# password = ''.join(random.sample(random.choice(LETTER['EN'])+random.choice(LETTER['dig'])+"".join(random.sample(LETTER['en'],lenght-2)), lenght))

# print(password)


# from string import *
# import random

# LETTER = {'EN': [x for x in ascii_uppercase if x not in 'OI'],
#           'en': [x for x in ascii_lowercase if x not in 'ol'],
#           'dig': [x for x in digits if x not in '01']}

# def generate_password(length):
#     password = ''.join(random.sample(random.choice(LETTER['EN'])+random.choice(LETTER['dig'])+"".join(random.sample(LETTER['en'],length-2)), length))
#     return password
# def generate_passwords(count, length):
#     for i in range(count):
#         print(generate_password(length))

# n, m = int(input()), int(input())

# generate_passwords(n,m)