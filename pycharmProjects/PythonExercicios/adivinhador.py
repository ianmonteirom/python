print('-=-' * 10, 'Adivinhe o número!', '-=-' * 10)
import random
from time import sleep

jogar = str(input('\033[36mEstá pronto para começar? Responda somente com \033[32msim \033[36m/\033[31m não\033[36m: ')).strip().lower()
print('\033[mPROCESSANDO...')
sleep(1)
s = 'sim' in jogar
n = 'não' in jogar
if s:
    dificuldade = str(input('Escolha uma dificuldade: easy, normal, hard: ').strip().lower())
    easy = 'easy' in dificuldade
    normal = 'normal' in dificuldade
    hard = 'hard' in dificuldade
    d1 = random.randint(1, 3)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 9)
    print('PROCESSANDO ESCOLHA...')
    sleep(1)
    if easy:
        print('Modo fácil? É sério?')
        sleep(1)
        print('Ok, escolhi um número de 1 a 3, você consegue acertá-lo? ')
        sleep(1)
        escolha = int(input('Digite um número de 1 a 3: '))
        print('PROCESSANDO ESCOLHA...')
        sleep(3)
        if escolha == d1:
            print(f'Você acertou, era o {escolha}, mas era o esperado jogando no fácil.')
        if escolha != d1:
            print(f'Haha, você errou no modo fácil! O número que eu escolhi era {d1}, melhore!')
    if normal:
        print('Normal? Legal, finalmente um jogo de verdade!')
        sleep(1)
        print('Vou pensar em um número de 1 a 6. Você consegue acertá-lo?')
        sleep(1)
        escolha = int(input('Escolha um número de 1 a 6: '))
        print('PROCESSANDO ESCOLHA...')
        sleep(3)
        if escolha == d2:
            print(f'Boa! Você acertou, eu realmente pensei no {escolha}. Te espero na dificuldade hard.')
        if escolha != d2:
            print(f'Boa tentativa, mas não foi dessa vez. Eu escolhi o número {d2}.')
    if hard:
        print('MODO HARD? Finalmente um oponente a altura! Nosso jogo será lendário!!')
        sleep(1)
        print('Escolhi um número de 1 a 9, quero ver se é capaz de me derrotar.')
        sleep(1)
        escolha = int(input('Escolha um número de 1 a 9: '))
        print('PROCESSANDO ESCOLHA...')
        sleep(3)
        if escolha == d3:
            print(f'{escolha}?? IMPOSSÍVEL!! Você realmente me derrotou, meus sinceros parabéns.' )
        if escolha != d3:
            print(f'Você errou, parece que te superestimei. O número que eu escolhi era {d3}. Volte ao modo difícil quando estiver melhor.')
if n:
    print('Medo ou respeito?...')

#else:
    #print('Escolha uma opção válida!')
print('-=-'*10, 'FIM DE JOGO', '-=-'*10)

