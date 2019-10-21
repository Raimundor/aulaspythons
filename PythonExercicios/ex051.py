print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for c in range(0, 10):
    print(termo, end=' -> ')
    termo += razao
print('ACABOU')

# do professor
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 -1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')