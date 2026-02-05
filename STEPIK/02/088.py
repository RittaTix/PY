# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# digits = {d for d in items if (items[d]).isdigit()}
# print(*sorted(digits))

# digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}
# print(digits)

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# digits = {int(d) for d in items}
# print(*sorted(digits))

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# pe_bu = {(d[0]).lower() for d in words}
# print(*sorted(pe_bu))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# for ch in "(),.;?!-:":
#     sentence = sentence.replace(ch, '')
# un_sl = {d.lower() for d in sentence.split() if len(d)<4}
# print(*sorted(un_sl))


# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# answer = {d.lower() for d in files if d[-4:].lower() == '.png'}
# print(*sorted(answer))
myset = {'intersection_update()','clear()','union()','discard()','intersection()','symmetric_difference_update()','pop()','difference()','update()','add()','difference_update()','remove()','symmetric_difference()'}
forozen = {j+'()' for j in dir(frozenset()) if j[-2:] != '__'}
print(*(myset - forozen), sep='\n')


set1 = frozenset('beegeek')
set2 = frozenset('stepik')

set3 = set1 & set2
print(set3)