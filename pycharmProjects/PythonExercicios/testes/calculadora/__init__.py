from time import sleep
from math import sqrt


def menu(msg):
    print('=' * len(msg))
    print(msg)
    print('=' * len(msg))


while True:
    cont = ' '
    resp, n, c, so, su, res, por = 0, 0, 0, 0, 0, 0, 0
    mu, di, po = 1, 1, 1
    nmrs = []
    ops = ['ADIÇÃO', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO', 'POTENCIAÇÃO']
    menu('CALCULADORA AUTOMÁTICA')
    print()
    sleep(0.5)
    print('Bem-vindo à Calculadora Automática. Qual operação deseja realizar?')
    print('[1] para ADIÇÃO\n'
          '[2] para SUBTRAÇÃO\n'
          '[3] para MULTIPLICAÇÃO\n'
          '[4] para DIVISÃO\n'
          '[5] para POTENCIAÇÃO\n'
          '[6] para RAIZ QUADRADA\n'
          '[7] para PORCENTAGEM\n'
          '[8] para SAIR')
    while True:
        try:
            print()
            sleep(1)
            print('-----------------------------------------------')
            resp = int(input('Escolha: '))
        except:
            print('Escolha uma opção válida!')
        else:
            break
    if resp == 8:
        menu('Obrigado por utilizar nosso programa!')
        break

    if resp == 1 or resp == 2 or resp == 3 or resp == 4 or resp == 5:
        while True:
            try:
                qnt = int(input('Com quantos números deseja realizar a operação? '))
            except:
                print('ERRO: Escolha uma quantidade de números!')
                sleep(0.5)
            else:
                break
        for c in range(1, qnt + 1):
            while True:
                try:
                    n = int(input(f'Digite o {c}° número: '))
                    nmrs.append(n)
                except:
                    print('ERRO: Escolha um número válido!')
                else:
                    break
        sleep(0.5)
        print(f'Números escolhidos para realizar a {ops[resp - 1]}: {nmrs}')
        if resp == 1:
            for c in range(0, qnt):
                so += nmrs[c]
                res = so
        elif resp == 2:
            for c in range(0, qnt):
                if c == 0:
                    su = nmrs[c]
                else:
                    su -= nmrs[c]
                    res = su
        elif resp == 3:
            for c in range(0, qnt):
                mu *= nmrs[c]
                res = mu
        elif resp == 4:
            for c in range(0, qnt):
                if c == 0:
                    di = nmrs[c]
                else:
                    di = di / nmrs[c]
                    res = di
        elif resp == 5:
            for c in range(0, qnt):
                if c == 0:
                    po = nmrs[c]
                else:
                    po **= nmrs[c]
                    res = po

    elif resp == 6:
        while True:
            try:
                n = int(input('Qual número deseja realizar a Raíz Quadrada? '))
            except:
                print('Erro! Escolha um número válido!')
            else:
                res = sqrt(n)
                break

    elif resp == 7:
        while True:
            try:
                n = int(input('Qual número deseja realizar a porcentagem? '))
            except:
                print('Erro! Escolha um número válido!')
            else:
                try:
                    por = int(input('Qual a porcentagem? '))
                except:
                    print('Erro! Escolha um número válido!')
                else:
                    po = (n * por) / 100
                    print(f'{por}% de {n}: {po}\n'
                          f'Valor descontado: {n - po}')
                    print()
                    print()
                    sleep(3)
                    break

    if resp != 7:
        sleep(0.5)
        menu(f'RESULTADO DA OPERAÇÃO: {res}')
        nmrs.clear()
        print()
        print()
        sleep(3)

    while cont not in 'sn':
        cont = str(input('Deseja realizar outra operação? [S/N] ')).strip().lower()
    if cont == 'n':
        menu('Obrigado por utilizar nosso programa!')
        break
