# Volume atual de um reservatório de água (em metros cúbicos)
reservoir_volume = 4.445e8
# Total de aágua da chuva de uma tempestade(em metros cúbicos)
rainfall = 5e6

# Reduza a variável de água da chuva(rainfall) em 10% para considerar perdas
rainfall *= 0.9
print('rainfall:', rainfall)

# Adicione a variável rainfall à variaável de vol. atual do reservatório(reservoir_volume)
reservoir_volume += rainfall
print('reservoir_volume:', reservoir_volume)

# aumente o volume do reservatório (reservoir_volume) em 5% para considerar águas tempestuosas
# que chegam no reservatório dias apoós a tempestade
reservoir_volume *= 1.05
print('reservoir_volume:', reservoir_volume)

# reduza o volume do reservatório (reservoir_volume) em 5% para considerar evaporaçaão
reservoir_volume *= 0.95
print('reservoir_volume:', reservoir_volume)

# Subtraia 2.5e5 metros cúbicos de reservoir_volume para considerar água
# que édirecionada para regiões áridas.
reservoir_volume -= 2.5e5
print('reservoir_volume:', reservoir_volume)

# execute um print do novo valor de reservoir_volume
print(reservoir_volume)

mv_population = 74728
mv_area = 11.995
mv_density = mv_population/mv_area
print(int(mv_density))
