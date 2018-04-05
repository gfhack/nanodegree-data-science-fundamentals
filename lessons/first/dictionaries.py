elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
elements['lithium'] = 3

print(elements['carbon'])

print('mithril' in elements)
print('adamantium' not in elements)

# quiz

population = {
    'Shanghai': 17.8,
    'Istanbul': 13.3,
    'Karachi': 13.0,
    'Mumbai': 12.5
}
print(population)

test = {1: 'vai', 1.1: 'brazil', 'test': 'am'}
print(test)

test.get(2)
print(test)
print(test.get(2))

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
