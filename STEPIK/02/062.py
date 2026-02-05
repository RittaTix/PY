# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)


# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
# k = numbers1*2 + numbers2*9 + numbers3
# print(k)

# city_name = input()
# city_year = int(input())
# city = (city_name,city_year)
# print(city)

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i if len(i) > 0 else 1 for i in tuples]
non_empty_tuples = [j for j in non_empty_tuples if j != 1]
print(non_empty_tuples)