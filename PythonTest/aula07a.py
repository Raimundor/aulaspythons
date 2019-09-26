n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}'.format(n1+n2))
print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m, d), end=' >>> ') # ,.:3f quantidade casas decimais
print('Divisão inteira  {} e \n potência {}'.format(di, e))
#\n quebra de linha e end='' juntar linha