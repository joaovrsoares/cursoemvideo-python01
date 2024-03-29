medida = float(input('Insira uma distancia em metros: '))
print(f'A medida de {medida}m corresponde a :')

# Cálculo e print de cada múltiplo de metro
km = medida / 1000
print(f'{km} km (quilômetro);')

hm = medida / 100
print(f'{hm} hm (hectômetro);')

dam = medida / 10
print(f'{dam} dam (decâmetro);')

# O próprio metro
print(f'{medida} m (metro);')

dm = medida * 10
print(f'{dm:.0f} dm (decímetro);')

cm = medida * 100
print(f'{cm:.0f} cm (centímetro);')

mm = medida * 1000
print(f'{mm:.0f} mm; (milímetro).')