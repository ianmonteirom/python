from time import sleep
n = cont = 0
while True:
    print('-'*30)
    cont = 0
    sleep(1)
    n = int(input('Quer ver a tabuada de qual valor? (Número negativo para parar) '))
    print('-'*30)
    if n < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n*cont}')
print('PROGRAMA TABUADA ENCERRADO. Obrigado por utilizar!')
