# hello
print('hello', "hello")

some_text = 'some string with "double quotes"'
print(some_text)

other_text = "some string with \"double quotes\""
print(other_text)

# concat
print('combine' + ' this ' + 'with this')

# multiplication
word = 'rome'
print(word * 5)

# length
number_of_characters = len('Udacity')
print(number_of_characters)

# quiz
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

log_message = username + ' accessed the site ' + url + ' at ' + timestamp + '.'
print(log_message)

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + ' ' + middle_names + ' ' + family_name)

driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
