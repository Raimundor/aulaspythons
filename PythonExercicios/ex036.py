casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do Comprador: R$ '))
ano = int(input('Quantos anos de financiamento? '))
prest = casa/(ano * 12)
minimo = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, ano, prest))
if prest <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')