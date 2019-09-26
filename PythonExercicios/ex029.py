v = float(input('Qual é a velocidade atual do carro? '))
lim = 80
mul = (v - 80) * 7
if v > lim:
    print('MULTADO! Você excedeu o limite permitido que é de {} km/h'
          '\nVocê deve pagar uma multa de R${:.2f}!'.format(lim, mul))
print('Tenha um bom dia! Dirija com segurança!') # condição simples, sem else
