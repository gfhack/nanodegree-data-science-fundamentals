# not useful
the_sun_is_up = True
the_sun_is_down = False
# not there yet
x = 42 > 43
print(x)

age = 18
is_young = age > 12 and age < 20
print(is_young)

not_young = not (age > 12 and age < 20)
print(is_young)

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population / sf_area
rio_de_janeiro_pop_density = rio_population / rio_area

#quiz
is_sf_denser_rf = san_francisco_pop_density > rio_de_janeiro_pop_density
print(is_sf_denser_rf)
