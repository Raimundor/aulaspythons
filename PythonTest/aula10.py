# Condições simples(só o if) e compostas (if e else)
n1 = float(input('Digite a primeria nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
# Condição simplificada
print('Parabéns' if m >= 6 else 'Estude mais')
