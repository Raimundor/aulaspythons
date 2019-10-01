sal = float(input('Qual é o salário do funcionário? R$ '))
if sal <= 1250:
    novo = (sal * 0.15) + sal
else:
    novo = (sal * 0.10) + sal
print('Quem ganhava \033[33mR${:.2f}\033[m passa a ganhar \033[31mR${:.2f}\033[m agora.'.format(sal, novo))
