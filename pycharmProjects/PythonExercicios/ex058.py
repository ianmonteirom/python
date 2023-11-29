from random import randint
reiniciar = 's'
print('-=' * 15, 'ADIVINHADOR 2.0', '-=' * 15)
print('Bem-vindo ao Adivinhador 2.0. Você já conhece como funciona o jogo?')
escolha1 = str(input('[S/N]: ')).strip().lower()
if escolha1 == 'n':
    print('O jogo é muito simples. Eu vou pensar em um número aleatório de 0 a 10, e você deverá acertar\n'
          ' qual número eu escolhi, só que dessa vez iremos até você acertar. Entendido?')
    escolha2 = str(input('[S/N]: ')).strip().lower()
    while escolha2 != 's':
        print(
            'É simples, você só precisa chutar um número de 0 a 10. Se for o mesmo que eu chutei, você ganha. Entendido?')
        escolha2 = str(input('[S/N]: ')).strip().lower()
print('--' * 20)
dado = randint(0, 10)
palp = 0
tent = 5
while reiniciar == 's':
    print('Muito bem! Vamos ao jogo. Eu acabei de escolher um número. Qual número eu pensei?')
    jogador = int(input('Escolha um número [ DE 0 ATÉ 10 ]: '))
    while jogador < 0 or jogador > 10:
        print('Escolha inválida! Escolha um número somente de 0 a 10.')
        jogador = int(input('Escolha um número [ DE 0 ATÉ 10 ]: '))
    if 0 <= jogador <= 10:
        while tent > 0:
            while jogador != dado:
                palp += 1
                if jogador > dado:
                    print(f'{jogador} é muito alto... Tente de novo.')
                if dado > jogador:
                    print(f'{jogador} é muito baixo... Tente de novo.')
                #print(f'{tent} tentativas restantes.')
                jogador = int(input('Escolha um número [ DE 0 ATÉ 10 ]: '))
                tent -= 1
if tent == 0:
    reiniciar = 'n'
    print('0 tentativas restantes. Você perdeu!')
    reiniciar = str(input('Deseja reiniciar o jogo? [S/N] ').lower()[0].strip())
    if jogador == dado:
        print('')
        print(f'Você venceu! Eu escolhi {dado} e você chutou {jogador}. Você chutou {palp+1} vezes para acertar.')
        reiniciar = str(input('Deseja reiniciar o jogo? [S/N] ').lower()[0].strip())
print('-='*15, 'FIM DE JOGO', '-='*15)
