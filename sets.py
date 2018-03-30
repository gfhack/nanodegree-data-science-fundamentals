countries = [
    'Angola',
    'Maldives',
    'India',
    'United States',
    'India',
    'Denmark',
    'Sweden'
]
print(countries)

countries_set = set(countries)
print(countries_set)
print('India' in countries_set)

countries_set.add('Italy')
print(countries_set)

# quiz
aa = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
bb = set(aa)
print(len(aa) - len(bb))

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

print(b)
