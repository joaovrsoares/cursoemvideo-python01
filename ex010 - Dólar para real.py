real = float(input('Quantos reais você tem na carteira? R$ '))
# Baseado na cotação de 29/03/2024:
dol = real * 5.02
print(f'Com R$ {real:.2f}, você pode comprar ${dol:.2f}.')
