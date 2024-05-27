from math import sin, cos, tan, radians
n = float(input('Digite um ângulo: '))
sin = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))
print(f'O seno de {n} tem valor {sin:.2f}, cosseno {cos:.2f}, e tangente {tan:.2f}.')
