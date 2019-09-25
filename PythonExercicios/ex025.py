nome = str(input('Qual o seu nome completo? ')).strip()
separado = nome.upper().split()
print('Seu nome tem Silva? {}'.format('SILVA' in separado))
