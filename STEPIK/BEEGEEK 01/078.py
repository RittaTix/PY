
# s = input()

# while len(s) < 10:
#     if len(s) % 4 == 0:
#         s = s + 'x'
#     elif len(s) % 5 == 0:
#         s = s + 'y'
#     else:
#         s = 'z' + s 

# s = '@' + s
# print(s)

num = int(input())
cnt = 0
total = 0
while num % 100 != 11:
    if len(num) > 7:
        cnt += 1

    total =+ 1
    num = int(input())

print(cnt, '/', total, sep='')