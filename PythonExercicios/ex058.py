from random import randint
comp = randint(0, 10)
palpites = 0
print('Sou seu computador...\nAcabei de pensar em número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
num = int(input('Qual é seu palpite? '))
while num != comp:
    if num < comp:
        num = int(input('Mais... Tente mais uma vez. '))
    else:
        num = int(input('Menos... Tente mais uma vez. '))
    palpites += 1
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

## do professor:
from random import randint
comp = randint(0, 10)
print('Sou seu computador...\nAcabei de pensar em número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    num = int(input('Qual é seu palpite? '))
    palpites += 1
    if num == comp:
        acertou = True
    else:
        if num < comp:
            print('Mais... Tente mais uma vez. ')
        elif num > comp:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))