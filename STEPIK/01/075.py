# name = input()

# while '_' not in name:
#     name = input()

# print(name)


# skolko_ludey = 0
# name = input()
# while name != "Александра":
#     name = input()
# while name != "Левон":
#     name = input()
#     skolko_ludey += 1
# print(skolko_ludey-1)

# h1 , m1 , h2 , m2 = int(input()), int(input()), int(input()), int(input())
# hm1 = h1 * 60 + m1
# hm2 = h2 * 60 + m2
# while hm1 <= hm2:
#     ch, m = hm1//60, hm1%60
#     if ch < 10:
#         ch = '0' + str(ch)

#     if m < 10:
#         m = '0' + str(m)
#     print(ch,m,sep=":")
#     hm1+=1

# num = 725
# while num != 0:
#     last_digit = num % 10
#     num //= 10
#     print(last_digit, sep='', end='$')

num = 586
while num > 0:
    last_digit = num % 10
    print(last_digit, sep='*', end='#')
    num //= 10
    print()