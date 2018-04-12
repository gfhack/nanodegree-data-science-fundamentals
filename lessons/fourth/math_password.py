import math
import random
print(math.exp(5))

word_file = "words.txt"
word_list = []

with open(word_file,'r') as words:
	for line in words:
		word = line.strip().lower()
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    list = ''
    for i in range(3):
        list += word_list[random.randint(0, len(word_list))]
    return list
# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces

# test your function
print(generate_password())
