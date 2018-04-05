manifest = [
    ("bananas", 15),
    ("mattresses", 24),
    ("dog kennels", 42),
    ("machine", 120),
    ("cheeses", 5)
]

cargo = []
weight = 0
maximum_capacity = 100

for cargo_name, cargo_weight in manifest:
    if weight > 100:
        break
    elif weight + cargo_weight > 100:
        continue
    else:
        cargo.append(cargo_name)
        weight += cargo_weight

print(cargo, weight)

# quiz

headlines = [
    "Local Bear Eaten by Man",
    "Legislature Announces New Laws",
    "Peasant Discovers Violence Inherent in System",
    "Cat Rescues Fireman Stuck in Tree",
    "Brave Knight Runs Away",
    "Papperbok Review: Totally Triffic"
]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + ' '
    if len(news_ticker) >= 140:
        break

news_ticker = news_ticker[:140]
print(news_ticker, len(news_ticker));
