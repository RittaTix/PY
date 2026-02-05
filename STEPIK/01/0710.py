# flag = False
# n, m = int(input()), int(input())
# for x in range (1,n):
#    for y in range (1,n):
#         for z in range (1,n):
#             if x + 3*y + 2*z == m:
#                 print(x,' + 3×',y,' + 2×',z,' = ',m, sep = '')
#                 flag = True
# if flag == False:
#     print("При заданных n и m решений не существует.")

n = int(input())
for h in range (0,24):
    for m in range (0,60):
        if int(h)**n == int(m):
            if len(str(h)) < 2:
                h = "0" + str(h)
            if len(str(m)) < 2:
                m = "0" + str(m)
            print(h, ":", m, sep = '') 






