'''for c in range(1,10):
    print(c)
print('fim')
c = 1
while c < 10:
    print(c)
    c += 1
print('Acabou')'''
n = 1
while n !=0:
    n = int(input('Digite um número: '))
print('acabou')
c = 'S'
while c == 'S':
    n = int(input('Digite um número: '))
    c = input('Deseja continuar: [S/N]: ').upper()
print('acabou')

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} impares'.format(par, impar))
