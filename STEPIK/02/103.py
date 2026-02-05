# dct = {'понедельник': 1, 'вторник': 2, 'среда': 3}

# print(dct.get('понедельник', 'Не найдено'))

# dct = {'понедельник': 1, 'вторник': 2, 'среда': 3}

# print(dct.get('пятница', 'Не найдено'))

# student = {'name': 'Rosaly',
#            'class': 10,
#            'marks': 75}

# del student

# print(student)

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
# print(result)

# dict = {}
# for i in range(1,16):
#     dict[i] = i**2
# print(dict)

# result = {}
# for i in range(1, 16):
#     result.setdefault(i, i ** 2)

# # Creating a dictionary (создаём словарь)
# fruits = {'apples': 5, 'oranges': 3}

# # Using setdefault to get the value of an existing key (с помощью setdefault получаем значение существующего ключа)
# apples_count = fruits.setdefault('apples', 10)
# print('Apples:', apples_count)


# # Using setdefault to add a new key with a default value (c помощью setdefault добавляем новый ключ со значением по умолчанию)
# bananas_count = fruits.setdefault('bananas', 10)
# print('Bananas:', bananas_count)


# # Printing the updated dictionary (выводим обновлённый словарь)
# print(fruits)

# dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
# dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}
# dict_result = {}
# for item1 in dict1:
#     if dict1[item1] not in dict_result:
#         dict_result[item1] = dict1[item1]
#     else:
#         dict_result[item1] = dict_result[item1] + dict1[item1]

# for item2 in dict2:
#     if dict2[item2] not in dict_result:
#         dict_result[item2] = dict2[item2]
#     else:
#         dict_result[item2] = dict_result[item2] + dict2[item2]


# print(dict_result)

# dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
# dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}
# dict_result = dict1

# for item in dict2:
    
#     if item in dict_result:
#         dict_result[item] = dict_result[item] + dict2[item]
#     else:
#         dict_result.setdefault(item,dict2[item])
       
# print(dict_result)

# text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
# dict_n = dict.fromkeys(text,0)
# for i in(dict_n):
#     dict_n[i] = text.count(i)
# print(dict_n)

# text = 'bridge snake island game glory eye arrogant car nature game glory game'
# set_text = set(text.split(" "))

# dict = {}

# for item in set_text:
    
#     if item in dict:
#         dict[item] += 1
#     else:
#         dict.setdefault(item,1)

# print(dict)

# text = 'bridge snake island game glory eye arrogant car nature game glory game'
# set_text = set(text.split(" "))
# print(set_text)
# dict = {}

# for item in set_text:
#     dict.setdefault(item,text.count(item))

# max_value = max(dict.values())

# for key, value in sorted(dict.items()):
#     if value == max_value:
#         key_found = key
#         break 

# print(key_found)

# pets = [
#     ('Барсик', 'Маша', 'Петрова', 17),
#     ('Джек', 'Галина', 'Лагунова', 45),
#     ('Муся', 'Александр', 'Каракулов', 28),
#     ('Буся', 'Маша', 'Петрова', 17),
#     ('Кира', 'Вова', 'Пухарев', 54),
# ]

# dict = {}
# for i in pets:
#     if i[1:] in dict:
#         #dict[i] += i[0]
#         print(1)
#     else:
#         #dict[1:] = i[0] 
#         #dict[1:] = list[i[0]]
#         dict.update(tuple(i[1:]))
# print(dict)

# pets = [
#     ('Барсик', 'Маша', 'Петрова', 17),
#     ('Джек', 'Галина', 'Лагунова', 45),
#     ('Муся', 'Александр', 'Каракулов', 28),
#     ('Буся', 'Маша', 'Петрова', 17),
#     ('Кира', 'Вова', 'Пухарев', 54),
# ]
# dict1 = {}

# for i in pets:
#     dict1[i[1:]] = []    

# dict2 = {}
# for j in pets:
#     if j[1:] in dict1:
#         dict2[j[1:]] = 
        
#         print(dict1[j[1:]]) 
       

# print(dict)
# # for item in dict:
# #     dict[item] = 
# #     print(item)


# pets = [
#     ('Барсик', 'Маша', 'Петрова', 17),
#     ('Джек', 'Галина', 'Лагунова', 45),
#     ('Муся', 'Александр', 'Каракулов', 28),
#     ('Буся', 'Маша', 'Петрова', 17),
#     ('Кира', 'Вова', 'Пухарев', 54),
# ]

# dict = {}

# for i in pets:
#     #dict[i[1:]] = []   

#     dict.setdefault(i[1:],[]) 
#     cur = dict.get(i[1:], []) 
#     cur.append(i[0]) 
#     dict[i[1:]] = cur


# # print(dict)
# word = "London is the capital of Great Britain. More than six million people live in London. London lies on both banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is not only the capital of the country, it is also a very big port, one of the greatest commercial centres in the world, a university city, and the seat of the government of Great Britain!"
# lst = [word.strip('.,!?:;-') for word in word.lower().split()]

# #print(lst)

# dict = {}
# for i in lst:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict.setdefault(i, 1)

# min_value = min(dict.values())

# for key, value in sorted(dict.items()):
#     if value == min_value:
#         key_found = key
#         break 
# print(key)

# dct = {}
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# for word in lst:
#     dct[word] = dct.get(word, 0) + 1
# lst = [(value, key) for key, value in dct.items()]
# lst.sort()
# print(lst[0][1])

# # print(dict)
# word = "London is the capital of Great Britain. More than six million people live in London. London lies on both banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is not only the capital of the country, it is also a very big port, one of the greatest commercial centres in the world, a university city, and the seat of the government of Great Britain!"
# lst = [word.strip('.,!?:;-') for word in word.lower().split()]

# #print(lst)

# dict = {}
# for i in lst:
#     dict[i] = dict.get(i,0)+1
# print(dict)
# min_value = min(dict.values())

# for key, value in sorted(dict.items()):
#     if value == min_value:
#         key_found = key
#         break 
# print(key)

# dct = {}
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# for word in lst:
#     dct[word] = dct.get(word, 0) + 1
# lst = [(value, key) for key, value in dct.items()]
# lst.sort()
# print(lst[0][1])


# Используем тот же метод, что и в предыдущих задачах: text_dic[i] = text_dic.get(i, 0) + 1, для подсчета количества повторений.
# Далее все просто, если значение по ключу больше одного (то есть этот элемент встречается больше одного раза):  if text_dic[i] > 1: добавляем в список строку из элемента  +"_" + (индекса повторения минус 1), вот выражение: text_new.append(i + "_" + str((text_dic[i] - 1))). 

# В противном случае, просто добавляем в список элемент (без индекса повторения).

sp = input().strip('.,?:;- ').split()
dict = {}
for i in sp:
    dict[i] = dict.get(i,0)+1
    if dict[i] == 1:
        print(i, end = " ")
    else:
        print(i + "_" + str(dict[i]-1), end = " ")



    
       

     

# В противном случае, просто добавляем в список элемент (без индекса повторения).