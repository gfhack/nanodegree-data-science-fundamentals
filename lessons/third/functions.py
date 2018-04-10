def cylinder_volume(height, radius = 5):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10))
print(cylinder_volume(10, 3))

# quiz
def population_density(population, area):
    return population / area

test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

# write your function here
def readable_timedelta(days):
    """ Return a readable time in week(s) and day(s). """
    week = days // 7
    day = days % 7
    return '{} week(s) and {} day(s).'.format(week, day)

print(readable_timedelta(1))
print(readable_timedelta(6))
print(readable_timedelta(7))
print(readable_timedelta(9))
print(readable_timedelta(1596))

# error
egg_count = 0
def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
print(egg_count)
