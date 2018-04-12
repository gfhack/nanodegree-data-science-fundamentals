how_many_snakes = int(input('How many snakes? '))
snake_string = """
             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/
"""


print(snake_string * how_many_snakes)

# quiz

names = input('Enter names separated by comas: ').title().split(',')
assignments = input('Enter assignments count separated by comas: ').split(',')
grades = input('Enter grades separated by comas: ').split(',')
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    message.format(name, assignment, grade, int(grade) + (int(assignment) * 2))
    print(message)
