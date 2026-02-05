# a,b,c = '2010', "10k", 'Bitcoin'
# s = f'In {a}, someone paid {b} {c} for two pizzas.'
# print(s)

# a = input()
# b = input() 
# c = input() 
# s = f'На {a}: 1€ = {b}₽, 1¥ = {c}₽'
# print(s)

# a = int(input())
# b = int(input())
# s0 = f'Для чисел {a} и {b}:'
# s1 = f'  Сумма кубов: {a}**3 + {b}**3 = {a**3 + b**3}'
# s2 = f'  Куб суммы: ({a} + {b})**3 = {(a + b)**3}'
# print(s0)
# print(s1)
# print(s2)

# dp = int(input())
# tv = float(input())
# ov = 100-dp*0.2
# if tv>ov:
#     print("Что-то пошло не так")
# else:
#     print("Все идет по плану")
# s = f'#{dp} ДЕНЬ: ТЕКУЩИЙ ВЕС = {tv} кг, ЦЕЛЬ по ВЕСУ = {ov} кг'

#print(ord('6'))

# letter = input()

# if ord(letter) < 1040 or ord(letter)>=1071:
#     print("Дальше букв нет")
# else:
#     print(chr(ord(letter)+1))


# a = int(input())
# b = int(input())

# for i in range (a, b+1):
#     print (chr(i), end = " ")

# s = input()
# for i in range (len(s)):
#     print(ord(s[i]), end = " ")

# a = input()
# b = input()
# c = input()
# d = input()

# lna = 0
# lnb = 0
# lnc = 0
# lnd = 0

# for i in range (len(a)):
#     lna = lna + ord(a[i])
    
# for i in range (len(b)):
#     lnb = lnb + ord(b[i])

# for i in range (len(c)):
#     lnc = lnc + ord(c[i])

# for i in range (len(d)):
#     lnd = lnd + ord(d[i]) 

# if max(lna, lnb, lnc, lnd) == lna:
#     print(a)
# elif max(lna, lnb, lnc, lnd) == lnb:
#     print(b)
# elif max(lna, lnb, lnc, lnd) == lnc:
#     print(c) 
# else:
#     print(d)              

# s = input()
# sum = 0
# for i in range(len(s)): 
#     sum+=ord(s[i])
# print("Текст сообщения: '", s,"'", sep = "")
# print("Стоимость сообщения: ", sum*3, chr(128029), sep = "" )

# s = input()
# en_alts, ru_alts = "eyopaxcETOPAHXCBM", "еуорахсЕТОРАНХСВМ"
# sum_old, sum_new = 0, 0
# for i in range(len(s)):
#     if  en_alts.find(s[i]) == -1:
#       sum_old += ord(s[i]) 
#       sum_new += ord(s[i])  
#     elif en_alts.find(s[i]) != -1:
#       sum_old += ord(s[i]) 
#       sum_new += ord(ru_alts[en_alts.find(s[i])])
# print("Старая стоимость: ", sum_old*3, chr(128029), sep = "")
# print("Новая стоимость: ",sum_new*3, chr(128029), sep = "")



a = int(input())
b = input()

for i in range(len(b)):
    n = ord(b[i])-a
    if n < 97:
        n = 122 -(96-n)
    print(chr(n), end="")