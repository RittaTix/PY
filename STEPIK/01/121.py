# sp1 = input().split()
# sp2 = input().split()
# sp3 =[]
# for i in range(len(sp1)):
#     sp3.append(int(sp1[i])+int(sp2[i]))
# print(*sp3)

# sp = input().split()
# for i in range(len(sp)):
#     sp[i] = int(sp[i])
# print(*sp, sep = "+", end = "=")
# print(sum(sp))

# sp = list(input())
# if len(sp) == 12 or len(sp) == 14:
#     if sp[0] == 7:
# else:
#     print("NO")

# sp = input().split()
# sp2 = []
# for i in range(len(sp)):
#     sp2.append(len(sp[i]))
# print(max(sp2))

sp = input().split()
for i in range(len(sp)):
    sp[i] = sp[i][1:] + sp[i][0] + "ки"
print(*sp)