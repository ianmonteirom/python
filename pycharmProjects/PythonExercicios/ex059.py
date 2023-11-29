from time import sleep
print('Bem-vindo a mini calculadora!')
continuar = str(input('Deseja realizar uma operação? [S/N]: '))
while continuar != 's' and continuar != 'n':
    print('Opção inválida!')
    continuar = str(input('Deseja realizar uma operação? [S/N]: '))
while continuar == 's':
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('')
    print('O que você deseja fazer com esses números?')
    print('')
    print('[ 1 ] para SOMAR\n'
          '[ 2 ] para MULTIPLICAR\n'
          '[ 3 ] para DESCOBRIR MAIOR VALOR\n'
          '[ 4 ] para INFORMAR NOVOS NÚMEROS\n'
          '[ 5 ] para SAIR DO PROGRAMA')
    print('')
    escolha = int(input('Digite sua escolha: '))
    while escolha >= 6 or escolha <= 0:
        print('Opção inválida! Escolha uma operação válida.')
        print('')
        print('O que você deseja fazer com esses números?')
        print('')
        print('[ 1 ] para SOMAR\n'
              '[ 2 ] para MULTIPLICAR\n'
              '[ 3 ] para DESCOBRIR MAIOR VALOR\n'
              '[ 4 ] para INFORMAR NOVOS NÚMEROS\n'
              '[ 5 ] para SAIR DO PROGRAMA')
        print('')
        escolha = int(input('Digite sua escolha: '))
        print('')
    while escolha == 4:
        print('')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print('')
        print('O que você deseja fazer com esses números?')
        print('')
        print('[ 1 ] para SOMAR\n'
              '[ 2 ] para MULTIPLICAR\n'
              '[ 3 ] para DESCOBRIR MAIOR VALOR\n'
              '[ 4 ] para INFORMAR NOVOS NÚMEROS\n'
              '[ 5 ] para SAIR DO PROGRAMA')
        print('')
        escolha = int(input('Digite sua escolha: '))
        print('')
    if escolha == 1:
        print(f'{n1} + {n2} = {n1+n2}.')
    if escolha == 2:
        print(f'{n1} x {n2} = {n1*n2}.')
    if escolha == 3:
        if n1 > n2:
            print(f'{n1} é o maior valor entre {n1} e {n2}.')
        elif n2 > n1:
            print(f'{n2} é o maior valor entre {n1} e {n2}.')
        elif n1 == n2:
            print('Ambos os valores são iguais.')
    if escolha == 5:
        print('Abortando operação...')
        print('--'*20)
    print('--'*20)
    continuar = str(input('Deseja realizar outra operação? [S/N]: '))
    print('')
print('Obrigado por utilizar nosso programa!')
sleep(0.5)
print('DESLIGANDO....')
print('--'*20)
