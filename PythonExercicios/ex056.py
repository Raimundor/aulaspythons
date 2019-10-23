somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    nome = str(input('----- {}ª PESSOA -----\nNome: '.format(p))).strip()
    idade = int(input('Idade: '.format(p)))
    sexo = str(input('Sexo [M/F]: '.format(p))).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': # pra não precisar do upper use in e coloca a letra maíuscula e ninuscula
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos 20 de anos'.format(totmulher))
