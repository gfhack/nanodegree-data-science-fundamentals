some_elements = {
    'hydrogen': {
        'number': 1,
        'weight': 1.00794,
        'symbol': 'H'
    },
    'helium': {
        'number': 2,
        'weight': 4.002602,
        'symbol': 'He'
    }
}

print(some_elements)

# quiz

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
elements['helium']['is_noble_gas'] = True
elements['hydrogen']['is_noble_gas'] = False

print(elements['helium']['is_noble_gas'])
print(elements['hydrogen']['is_noble_gas'])
