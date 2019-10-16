from datetime import date
gene = input('''Digite [M] para Masculino [F] para Feminino: ''').upper()

if gene == 'F':
    print('Não é obrigatório o alistamento')
else:
    nasc = int(input('Ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano ))
    if idade < 18:
        saldo = 18 - idade
        print('Ainda falta {} anos para o alistamento'.format(saldo))
        alist = ano + saldo
        print('Seu alistamento será em {}'.format(alist))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        alist = ano - saldo
        print('Seu alistamento foi em {}'.format(alist))
    else:
        print('Você tem que se alistar IMEDIATAMENTE')
