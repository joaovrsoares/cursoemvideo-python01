altura = float(input('Digite a altura da parede em m²: '))
largura = float(input('Digite a largura da parede em m²: '))
area = altura * largura
tinta = area / 2
print(f'Sua parede tem altura de {altura}x{largura}m, totalizando área de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta} litros de tinta.')
