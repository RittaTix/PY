# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# lengths = [len(keywords[i]) for i in range(len(keywords))]

# print(lengths)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [i for i in keywords if len(i)>=5]

# print(new_keywords)

# palindromes = [i for i in range(100,1000) if i % 10 == i // 100]

# print(palindromes)

# n = int(input())
# sp = [i**2 for i in range(1,n+1)]
# print(*sp, sep = "\n")

# numbers = input().split()
# for i in range(len(numbers)): 
#     numbers[i] = int(numbers[i])
# print(numbers)


# numbers = input().split()
# sp = [int(numbers[i])**3 for i in range(len(numbers))]
# print(*sp)

# print(*(input().split()), sep = "\n")

# s = list(input())
# print(*(i for i in s if i.isdigit()), sep = "")

# numbers = input().split()
# sp = [int(numbers[i])**2 for i in range(len(numbers)) if(int(numbers[i])%2 == 0 and ((int(numbers[i])**2))%10 != 4)]
# print(*sp)

team = ['Arthur', 'Timur', 'Anton', 'Valera', 'Arthur', 'Sveta']
lengths = [len(name) for name in team]

print(*lengths)