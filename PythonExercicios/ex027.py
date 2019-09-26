nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Muito prazer te conhecer! \n'
      f'Seu primeiro nome é {lista[0]} \n'
      f'Seu último nome é {lista[-1]}')
# ou lista[len(lista)-1]
