cities = [
    'new york city',
    'mountain view',
    'chicago',
    'los angeles'
]

capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

else_squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(else_squares)

# quiz

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

multiples_3 = [x for x in range(3, 61) if x % 3 == 0]
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name in scores if scores[name] > 65]
print(passed)
