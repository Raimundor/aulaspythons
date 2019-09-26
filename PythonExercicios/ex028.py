from random import randint
from time import sleep
comp = randint(0, 5) # faz o computador 'pensar'
print('-=-'* 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-'* 20)
num = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO....')
sleep(2) # pra dar a impressão que está 'processando'
if num == comp:
    print('PARABÉNS!! Você conseguiu me vencer!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(comp, num))
