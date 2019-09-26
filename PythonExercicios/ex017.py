import math

cao = float(input('Comprimento do cateto oposto: '))
caa = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cao, caa)
print(f'A hipotenusa vai medir {hip:.2f}')
