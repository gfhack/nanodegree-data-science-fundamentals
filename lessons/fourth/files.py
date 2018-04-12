file = open('names.txt', 'r')
contents = file.read()
file.close()

print(contents)

file = open('another.txt', 'w')
file.write('someone')
file.close()

with open('names.txt', 'r') as file:
    print(file.read())

with open('camelot.txt') as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

# quiz

def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as f:
        for line in f:
            name = line.split(',')[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
