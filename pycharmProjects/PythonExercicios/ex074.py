from random import randint
'''maior = menor = 0
print(f'Os valores sorteados foram: ', end='')
for r in range(1, 6):
    rand = randint(1, 10)
    print(f'{rand}', end=' ')
    if r == 1:
        maior = menor = rand
    else:
        if rand > maior:
            maior = rand
        if rand < menor:
            menor = rand
print(f'\nO maior valor sorteado foi {maior}\n'
      f'O menor valor sorteado foi {menor}')'''

sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = 0
print(f'Os valores sorteados foram:', end=' ')
for c in sorteio:
    print(c, end=' ')
    #if c == sorteio[0]:
    #    maior = menor = c
    #else:
    #    if c > maior:
    #        maior = c
    #    if c < menor:
    #        menor = c
print(f'\nO maior valor sorteado foi {max(sorteio)}\n'
      f'O menor valor sorteado foi {min(sorteio)}')
