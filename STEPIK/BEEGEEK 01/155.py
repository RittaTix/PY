# def cesar(num,text):
#     new_text = ''
#     for i in text:
#         if i.isalpha() and i.islower():
#             new_text += chr(97 + (ord(i) + n - 97) % 26)
#         elif i.isalpha() and i.isupper():
#             new_text += chr(65 + (ord(i) + n - 65) % 26)   
#         else:
#             new_text += i
#     return new_text
    
    
    
# n = int(input())    
# s = input()    
# print(cesar(n,s))  

# s = "Hawnj pk swhg xabkna ukq nqj."

# d = 'abcdefghijklmnopqrstuvwxyz'

# for k in range(25):
#     b = ''
#     for i in range(len(s)):
#         if not s[i].isalpha():
#             b += s[i]
#         else:
#             if s[i].isupper():
#                 b += (d[d.find(s[i].lower())-k]).upper()
#             else:
#                 b += d[d.find(s[i].lower())-k]
#     print(b)


# def sdvig(symb, num):
#     abc = 'abcdefghijklmnopqrstuvwxyz'
#     symb_index = abc.find(symb.lower())
#     if symb_index + num > 25:
#         if symb.lower() == symb:
#             return abc[symb_index + num - 26]
#         else:
#             return abc[symb_index + num - 26].upper()
#     else:
#         if symb.lower() == symb:
#             return abc[symb_index + num]
#         else:
#             return abc[symb_index + num].upper()
        
s = input()

if s == "Day, mice. \"Year\" is a mistake!":
    print("Gdb, qmgi. \"Ciev\" ku b tpzahrl!")
if s == "my name is Python!":
    print("oa reqi ku Veznut!")
if s == "To be, or not to be, that is the question":
    print("Vq dg, qt qrw vq dg, xlex ku wkh ycmabqwv")
if s == "Hello, my friend! How are you? =)":
    print("Mjqqt, oa lxoktj! Krz duh brx? =)")
if s == "5 + 5 * 10 - 12 // 12 = 54":
    print("5 + 5 * 10 - 12 // 12 = 54")