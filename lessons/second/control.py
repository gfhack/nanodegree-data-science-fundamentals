bank_balance = 100
phone_balance = 0

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)

n = 3

if n % 2 == 0:
    print('even')
else:
    print('odd')

season = 'season'

if season == 'spring':
    print('allergy')
elif season == 'summer':
    print('hot')
elif season == 'fall':
    print('leaves')
elif season == 'winter':
    print('cold')
else:
    print('tornado')

# quiz
points = 174  # use this input when submitting your answer

if points > 1 and points <= 50:
    prize = 'wooden rabbit'
elif points > 51 and points <= 150:
    prize = 'no prize'
elif points > 151 and points <= 180:
    prize = 'wafer-thin mint'
elif points > 181 and points <= 200:
    prize = 'penguin'

result = "Congratulations! You won a " + prize + "!"
print(result)

weight = 80
height = 1.9

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

is_sunny = True
is_raining = False

if is_raining and is_sunny:
    print("Is there a rainbow?")

location = 'BR'
unsubscribed = False

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")

# quiz

altitude = 10000
speed = 250
propulsion = "Propeller"

print('------------------------------------')

if altitude < 1000 and speed > 100:
    print(True)
else:
    print(False)

if (propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000:
    print(True)
else:
    print(False)

if not (speed > 400 and propulsion == "Propeller"):
    print(True)
else:
    print(False)

if (altitude > 500 and speed > 100) or not propulsion == "Propeller":
    print(True)
else:
    print(False)

print('------------------------------------')
points = 174
prize = None

if points <= 50:
    prize = 'wooden rabbit'
elif points <= 180:
    prize = 'wafer-thin mint'
else:
    prize = 'penguin'

if prize:
    result = "Congratulations! You won a " + prize + "!"
else:
    result = "Oh dear, no prize this time."

print(result)
