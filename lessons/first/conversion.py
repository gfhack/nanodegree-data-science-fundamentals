house_number = 13
street_name = 'The Crescent'
town_name = 'Belmont'

print(type(house_number))

address = str(house_number) + ' ' + street_name + ', ' + town_name
print(address)

grams = '35.0'
print(type(grams))
grams = float(grams)
print(type(grams))

print(type("hippo" * 12))

# quiz

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

mon_sales = int(mon_sales)
tues_sales = int(tues_sales)
wed_sales = int(wed_sales)
thurs_sales = int(thurs_sales)
fri_sales = int(fri_sales)

total_sales = mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales
this_week_sales = "This week's total sales: " + str(total_sales)
print(this_week_sales)
