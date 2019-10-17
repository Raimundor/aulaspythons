print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - preço * 0.10
elif opção == 2:
    total = preço - preço * 0.05
elif opção == 3:
    total = preço
    vl_parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(vl_parcela))
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    total = preço + preço * 0.20
    vl_parcela = total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, vl_parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
