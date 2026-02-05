# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sum = 0
# for i in range(len(numbers)):
#     sum += numbers[i]**2
# print(sum)

# n = int(input())
# sp = []
# ur = []
# for i in range(n):
#     ch = int(input())
#     sp.append(ch)
#     ur.append(ch**2+2*ch+1)

# print(*sp, sep = '\n')
# print()
# print(*ur, sep = '\n')

# n = int(input())
# sp = []
# for i in range(n):
#     sp.append(int(input()))
# sp.remove(max(sp))
# sp.remove(min(sp))
# print(*sp, sep = "\n")

# n = int(input())
# sp = []
# for i in range(n):
#     w = input()
#     if w not in sp:
#         sp.append(w)
# print(*sp, sep = "\n")

# n = int(input())
# sp = []
# for i in range(n):
#     sp.append(input())
# z = input()

# for j in range(len(sp)):
#     if z.lower() in sp[j].lower():
#         print(sp[j])

# n = int(input())
# sp1 = []
# for i in range(n):
#     sp1.append(input())

# k = int(input())
# sp2 = []
# for j in range(k):
#     z = input()
#     if z.lower() in sp1.lower():

# sp1 = ['Язык Python прекрасен', 'C# - отличный язык программирования', 'Stepik - отличная платформа', 'BEEGEEK FOREVER!', 'язык Python появился 20 февраля 1991']
# sp2 = ['язык', 'python']

# n = int(input())
# sp1 = []
# for i in range(n):
#     sp1.append(input())

# k = int(input())
# sp2 = []
# for i in range(k):
#     sp2.append(input())

# sp3 = []

# for h in range(len(sp1)):
#     count = 0
#     for g in range(len(sp2)):
#        if sp2[g].lower() in sp1[h].lower():
#            count +=1
#     if count == len(sp2):
#         sp3.append(sp1[h])        
# print(*sp3, sep = "\n")  
  
  
  
    # for j in range (len(sp2)):
    #     if sp2[j].lower() in sp1[i].lower():
    #         print("1")
    

n = int(input())
sp1 = []
sp2 = []
sp3 = []
for i in range(n):
    ch = int(input())
    if ch < 0:
        sp1.append(ch)
    if ch == 0:
        sp2.append(ch)
    if ch > 0:
        sp3.append(ch)
print(*sp1, sep = "\n")
print(*sp2, sep = "\n")
print(*sp3, sep = "\n")