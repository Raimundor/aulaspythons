n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO.')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')