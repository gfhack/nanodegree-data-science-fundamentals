some_list = [
    'some text',
    'other text',
    'a text',
    'zeta text'
]

print(some_list)
print(min(some_list))
print(max(some_list))
print(sorted(some_list))

print(' - '.join(some_list))
some_list.append('more text')
print(some_list)

# quiz
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
