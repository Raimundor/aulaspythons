from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input(' [1] somar\n [2] multiplicar\n [3] maior\n [4] novos números\n [5] sair do programa'
                  '\n>>>>> Qual é sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-='*10)
    sleep(1)
print('Fim do programa! Volte sempre!')
