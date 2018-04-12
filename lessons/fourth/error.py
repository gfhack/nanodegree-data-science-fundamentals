# list = {'qualquer': 'coisa'}
#
# try:
#     print(list['outra'])
# except KeyboardInterrupt as k:
#     print('ué')
# except Exception as e:
#     print(list['qualquer'])
# finally:
#     print('crash')

# quiz
def create_groups(items, n):
    """Splits items into n groups of equal size, although the last one may be shorter."""
    try:
        size = len(items) // n
    except ZeroDivisionError as z:
        print("ZeroDivisionError occurred: {}".format(z))
        print("0 groups returned.")
        return []

    # create each group and append to a new list
    groups = []
    for i in range(0, len(items), size):
        groups.append(items[i:i + size])

    # print the number of groups and return groups
    print("{} groups returned.".format(n))
    return groups

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
