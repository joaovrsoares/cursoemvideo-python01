dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = (dias * 60) + (km * 0.15)

print(f'Considerando que:')
print(f'Total de dias alugados: {dias}')
print(f'Total de km rodados: {km:.1f}')
print(f'Total devido: R$ {total:.2f}')
