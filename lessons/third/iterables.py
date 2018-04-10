def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

 # quiz

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    i = 0
    while i < len(iterable):
        yield start, iterable[i]
        i += 1
        start += 1

# for i, lesson in my_enumerate(lessons, 1):
#     print("Lesson {}: {}".format(i, lesson))
#
# for i, lesson in my_enumerate(['a', 'b', 'c']):
#     print("Lesson {}: {}".format(i, lesson))
#
# for i, lesson in my_enumerate(['a', 'b', 'c'], 6):
#     print("Lesson {}: {}".format(i, lesson))

def chunker(iterable, size):
    i = 0
    loop = 1
    chunk = []
    while i < len(iterable):
        chunk.append(iterable[i])
        i += 1
        if i > (size * loop) - 1:
            yield chunk
            loop += 1
            chunk = []
    yield chunk

def chunking(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))
for chunk in chunking(range(25), 4):
    print(list(chunk))

for chunk in chunker('python programming', 5):
    print(list(chunk))
for chunk in chunking('python programming', 5):
    print(list(chunk))

sq_list = [x**2 for x in range(10)]      # this produces a list of squares
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
