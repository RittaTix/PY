# set1 = {10, 20, 30, 40}
# set2 = {50, 20, '10', 60}

# set3 = set1.union(set2)

# print(len(set3))

# set1 = {'Yellow', 'Orange', 'Black'}
# set2 = {'Orange', 'Blue', 'Pink'}

# set3 = set2.difference(set1)
# print(set3)


# set1 = {'Yellow', 'Orange', 'Black'}
# set2 = {'Orange', 'Blue', 'Pink'}

# set1.difference_update(set2)
# print(set1)

# myset = {'Yellow', 'Orange', 'Black'}

# myset.update(['Blue', 'Green', 'Red', 'Orange'])
# print(myset)

myset = {'Yellow', 'Orange', 'Black'}
myset.discard('Blue')

print(myset)