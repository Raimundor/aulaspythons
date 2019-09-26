sal = float(input('Qual é o salário do Funcionário? R$ '))
nsal = sal + (sal * 15 / 100)
print(f'Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, passa a receber R${nsal:.2f}')
