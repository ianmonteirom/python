from random import choice
from time import sleep
print('\033[32m-=\033[m'*15, '\033[36mJOKENPÔ\033[m', '\033[32m-=\033[m'*15)
sleep(1)
print('Bem-vindo ao simulador de Jokenpô. Você já conhece as regras do jogo?')
sleep(1)
regras = str(input('Digite "sim" para ir direto ao jogo e "não" para ler as regras: ')).strip().lower()
sleep(1)
s = 'sim' in regras
n = 'não' in regras
if n:
    print('As regras são muito simples. Eu vou escolher entre pedra, papel ou tesoura, e você deve escolher um entre os três também.\n'
          'Pedra ganha de Tesoura, Tesoura ganha de Papel e Papel ganha de Pedra. Bem simples, não?')
    sleep(6)
    e1 = str(input('Preparado para jogar agora? (s/n): '))
    sleep(1)
    s = 's' in e1
    n = 'n' in e1
    if n:
        print('Tudo bem. Volte quando quiser.')
if s:
    ec = choice(['pedra', 'papel', 'tesoura'])
    print(f'Muito bem. Eu acabei de fazer a minha escolha. Qual vai ser a sua?')
    sleep(2)
    ej = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).strip().lower()
    #print(f'Sua escolha: {ej}')
    a = 'pedra' in ej
    b = 'papel' in ej
    c = 'tesoura' in ej
    print('PROCESSANDO ESCOLHA...')
    sleep(3)
    if ec == 'pedra' and b:
        print(f'Parabéns, você venceu! Eu escolhi pedra e você escolheu papel.')
    elif ec == 'pedra' and a:
        print(f'Empate! Ambos jogamos pedra.')
    elif ec == 'pedra' and c:
        print(f'Você perdeu! Eu escolhi pedra e você escolheu tesoura.')
    elif ec == 'papel' and b:
        print(f'Empate! Ambos jogamos papel.')
    elif ec == 'papel' and a:
        print(f'Você perdeu! Eu escolhi papel e você escolheu pedra.' )
    elif ec == 'papel' and c:
        print(f'Parabéns, você venceu! Eu escolhi papel e você escolheu tesoura.')
    elif ec == 'tesoura' and b:
        print(f'Você perdeu! Eu escolhi tesoura e você escolheu papel.')
    elif ec == 'tesoura' and a:
        print(f'Parabéns, você venceu! Eu escolhi tesoura e você escolheu pedra.')
    elif ec == 'tesoura' and c:
        print(f'Empate! Ambos jogamos tesoura.')
    else:
        print('Escolha entre pedra, papel ou tesoura!')
else:
    print('Escolha uma opção válida!')
sleep(1)
print('\033[32m-='*15, '\033[31mFIM DE JOGO', '\033[32m-='*15 )





