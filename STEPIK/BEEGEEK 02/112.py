# DNA_RNA = {"G": "C", "C": "G", "T": "A", "A": "U"}
# for i in input():
#     print(DNA_RNA[i], end="")

# sp = input().split()
# result = {}
# for i in sp:
#     result[i] = result.get(i, 0) + 1
#     print(result[i],end=" ")

# d = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

# str = input()
# stoimost = 0
# for i in str:
#     stoimost += d[i]
# print(stoimost)

# def build_query_string(params):
#     sp = sorted(params.keys())
#     stroka = ""
#     for i in sp:
#         stroka = stroka + i + "=" + str(params[i]) + "&"
#     return stroka[:-2]


# def merge(values):      # values - это список словарей
#     pass

# values = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
# dict = {}
# for i in values:
#     for key, value in i.items():
#         dict.setdefault(key, set()).add(value)

# print(dict)

# s = {'W':'write' ,'R' :'read' ,'X':'execute' }
# prava = {}
# for i in range(int(input())):
#     pr = input().split()
#     prava.setdefault(pr[0], [s[z] for z in pr[1:]])
# print(prava)
# faily = {}

# for j in range(int(input())):
#     f = input().split()
#     if f[0] in prava[f[1]]:
#         print("OK")
#     else:
#         print("Access denied")

# dict = {}
# for i in range(int(input())):
#     sp = input().split()   
#     if tuple(sp[:2]) in dict.keys():
#         dict[tuple(sp[:2])] += int(sp[2])
#     else:
#         dict.setdefault(tuple(sp[:2]),int(sp[2]))
    
# print(dict)

dict = {('Вячеслав', 'Ручка'): 30, ('Филипп', 'Ручка'): 1, ('Виктория', 'Перо'): 3, ('Вячеслав', 'Линейка'): 4, ('Виктория', 'Тетрадь'): 7, ('Филипп', 'Циркуль'): 1}
pokypateli = sorted({z[0] for z in dict})
print(pokypateli)
for m in pokypateli:
    print(m + ":")
    for l,k in sorted(dict.items()):
        if m in l:
            print(l[1], k)



# dict_f = {}

# for k,v in dict.items():
#     dict_f.setdefault(k[0],(k[1]) + " " + str(v))
#     print()
# print(dict_f)
#print(dict_f)
# 

# perechen = {x: "777" for x in pokypateli}

# print(perechen)

buyers = {}
for _ in range(int(input())):
    name, product, number = input().split()    # разбираем строку на молекулы
    buyers.setdefault(name, {})    # если вдруг человек еще не покупал, создаем ему пустой список товаров
    buyers[name][product] = buyers[name].get(product, 0) + int(number)    # товар в словарь, а если он есть плюсуем

for buyer in sorted(buyers):      # тут мешанина из сортировок людей, коней и их слияния с количеством
    print(buyer + ':')            # через месяц фиг поймешь
    print(*(f'{key} {val}' for key, val in sorted(buyers[buyer].items())), sep='\n')
