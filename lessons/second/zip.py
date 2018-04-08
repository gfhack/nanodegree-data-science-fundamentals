zipped = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(zipped)

# pack
nums = [1, 2, 3]
letters = ['a', 'b', 'c']

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# unpack
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# quiz
print('------------------------------')

labels =  ["F", "J", "A", "Q", "Y", "B", "W", "X"]
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]

points = []

for i, label in enumerate(labels):
    points.append("{}: {}, {}, {}".format(label, x_coord[i], y_coord[i], z_coord[i]))

for point in points:
    print(point)

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))

print(cast)

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)

print(names)
print(heights)

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(tuple(i) for i in zip(*data))
print(data_transpose)

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, name in enumerate(cast):
    cast[i] = name + ' {}'.format(heights[i])
print(cast)
