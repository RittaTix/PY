num = str(int(input()))
chetnye = 1
while len(num) > 0:
    if int(num[0])%2 == 0:
        print(chetnye,"-я четная цифра равна ", num[0], sep = "") 
        chetnye += 1
    num = num[1:]
if chetnye == 1:
    print("Четных цифр в числе нет")


