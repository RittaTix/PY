# d = {}
# d['foo'] = 100
# d['bar'] = 200
# d['baz'] = 300

#d = dict(foo=100, bar=200, baz=300)

#d = {('foo', 100), ('bar', 200), ('baz', 300)}

#d = dict([('foo', 100), ('bar', 200), ('baz', 300)])

# d = {'foo': 100, 'bar': 200, 'baz': 300}
# print(d)
# print(type(d))

# data = [
#     'a',
#     'b',
#     {
#         'foo': 1,
#         'bar':
#         {
#             'x' : 10,
#             'y' : 20,
#             'z' : 30
#         },
#         'baz': 3
#     },
#     'c',
#     'd'
# ]

# print(data[2]['bar']['z'])


# data = [
#     'a',
#     'b',
#     {
#         'foo': 1,
#         'bar':
#         {
#             'x' : 10,
#             'y' : 20,
#             'z' : 30
#         },
#         'baz': 3
#     },
#     'c',
#     'd'
# ]

# print('z' in data[2])

# recipients = {
#     'Humanities': 409,
#     'Biology': 1473,
#     'Engineering': 1343,
#     'Physical Sciences': 1131,
#     'Medicine': 153,
#     'Scripps': 131,
#     'Social Sciences': 2870,
# }

# print(len(recipients))
# student = {'name': 'Emma', 'class': 9, 'marks': 75}
# print(student.get('marks'))
# print(student.get(2))
# #print(student[2])
# print(student['marks'])


# recipients = {
#     'Humanities': 409,
#     'Biology': 1473,
#     'Engineering': 1343,
#     'Physical Sciences': 1131,
#     'Medicine': 153,
#     'Scripps': 131,
#     'Social Sciences': 2870,
# }

# print(recipients['Math'])

# recipients = {
#     'Humanities': 409,
#     'Biology': 1473,
#     'Engineering': 1343,
#     'Physical Sciences': 1131,
#     'Medicine': 153,
#     'Scripps': 131,
#     'Social Sciences': 2870,
# }

# print(recipients.get('Math'))

# student = {'name': 'Emma', 'class': 9, 'marks': 75}	
# student.pop('class')	
# print(student)

# student = {'name': 'Emma', 'class': 9, 'marks': 75}	
# del student['class']	
# print(student)

# student = {'name': 'Emma', 'class': 9, 'marks': 75}	
# student.popitem()	
# print(student)


# recipients = {
#     'Humanities': 409,
#     'Biology': 1473,
#     'Engineering': 1343,
#     'Physical Sciences': 1131,
#     'Medicine': 153,
#     'Scripps': 131,
#     'Social Sciences': 2870,
# }

# for i in recipients.values():
#     print(i)

# my_dict = {
#     'math_grades': [10, 7, 36, 14, 25], 'physics_grades': [14, 28, 7, 10, 36, 5],
#     'chemistry_grades': [10, 14, 19, 20, 21], 'geography_grades': [10, 15, 19, 34],
# }

# my_dict = {k:[i for i in v if i <= 20] for k,v in my_dict.items()}
# print(my_dict)


# #z for z in my_dict[i] if int(z) <= 20


emails = {
    'stepik.org': ['help', 'support'],
    'pygen.ru': ['support', 'timur', 'soslan'],  
    'att.net': ['james_h', 'olivia_s', 'vitalik_b'],
    'yahoo.com': ['nicole52', 'meee55', 'pygen_official'],
}

f_emails = []

for k,v in emails.items():
    for i in v:
        f_emails.append(i+"@"+k)

print(*sorted(f_emails), sep='\n')