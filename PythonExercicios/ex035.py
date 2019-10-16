print('\033[33m-=\033[m' * 20)
print('\033[0;34mAnalisador de Triângulos\033[m')
print('\033[33m-=\033[m' * 20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os segmentos acima \033[34mPODEM FORMAR\033[m triângulo.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo.')