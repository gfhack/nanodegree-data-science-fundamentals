names = ['first', 'second', 'third', 'last']
print(names[0])
print(names[-1])

print(names[:2])
print(names[1:3])
print(names[2:])

print('first' in names)

names[3] = 'another one'

print(names)

# quiz
eclipse_dates = [
    'June 21, 2001',
    'December 4, 2002',
    'November 23, 2003',
    'March 29, 2006',
    'August 1, 2008',
    'July 22, 2009',
    'July 11, 2010',
    'November 13, 2012',
    'March 20, 2015',
    'March 9, 2016'
]

last_three_elements = eclipse_dates[-3:]
print(last_three_elements)

sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

#sentence2[6]= '!'
#sentence2[0]= "Our Majesty"
sentence2[0:2] = ["We", "want"]
print(sentence2)
