card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)

limit = 40

while not (limit ** (1/2)).is_integer():
    limit -= 1

nearest_square = limit

print(nearest_square)
