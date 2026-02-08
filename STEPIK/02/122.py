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

from random import shuffle
word = list("вау")
shuffle(word)
print(''.join(word))