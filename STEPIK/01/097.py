s = input()
while s.count("]")>0:
    pe = s.find("[")
    po = s.find("]")
    k = chr(int(s[(pe+3):po]))
    s = s.replace(s[pe:(po+1)],k)   
print(s)



# s = s.replace(str(k),chr(k))
# s = s.replace(s[po],"")
# s = s.replace(s[pe:(pe+3)],"")