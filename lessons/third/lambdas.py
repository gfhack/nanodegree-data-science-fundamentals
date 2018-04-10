def double(x):
    return x * 2

double = lambda num: num * 2
multiply = lambda x, y: x * y

print(double(2))
print(multiply(2, 3))

# quiz
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

averages = list(map(lambda list: sum(list) / len(list), numbers))
print(averages)

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(lambda city: len(city) < 10, cities))
print(short_cities)
