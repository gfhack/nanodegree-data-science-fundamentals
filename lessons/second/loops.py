cities = [
    'new york city',
    'mountain view',
    'chicago',
    'los angeles'
]

for city in cities:
    print(city.title())

for index in range(0, len(cities), 1):
    print(cities[index].title())

# quiz

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(names)):
    usernames[index] = usernames[index].lower().replace(' ', '_')

print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens:
    count += token.count('<')

print(count)

items = ['first string', 'second string']

html_str = "<ul>\n"
for item in items:
    html_str += "<li>" + item + "</li>\n"
html_str += "</ul>"

print(html_str)
