from random import randint
from time import sleep
n = randint(0, 5)
print('-=-'*20)
print('Pensei em um número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
escolha = int(input('Qual número de 0 a 5 eu escolhi? '))
print('PROCESSANDO...')
sleep(3)
if n == escolha:
    print('Parabéns, você acertou! A resposta era {}.'.format(n))
else:
    print('Resposta errada! O número que eu tinha escolhido era {}.'.format(n))
print('-=-'*10, 'FIM DE JOGO', '-=-'*10)
