from random import randint
print('-='*10)
print('PAR OU ÍMPAR')
print('-='*10)
computador = streak = 0
resultado = ''
while True:
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'pi':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    computador = randint(1, 10)
    soma = jogador + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    elif soma % 2 != 0:
        resultado = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}')
    print('-'*20)
    if resultado == 'PAR' and escolha == 'p' or resultado == 'ÍMPAR' and escolha == 'i':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-='*10)
        streak += 1
    elif resultado == 'PAR' and escolha == 'i' or resultado == 'ÍMPAR' and escolha == 'p':
        print('Você PERDEU!')
        print('-='*10)
        break
if streak == 0:
    print(f'GAME OVER! Você perdeu de primeira.')
elif streak == 1:
    print(f'GAME OVER! Você venceu {streak} vez.')
elif streak > 1:
    print(f'GAME OVER! Você venceu {streak} vezes.')
