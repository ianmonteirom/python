valores = []
cont = 0
while True:
    num = valores.append(int(input('Digite um número: ')))
    cont += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar == 'n':
        break
print('-='*20)
print(f'Você digitou {cont} números\n'
      f'A lista dos valores de forma decrescente é {valores.reverse()}')
if 5 in valores:
    print(f'O valor 5 foi digitado {valores.count(5)} vezes e aparece pela primeira vez na posição {valores.index(5)}')
elif 5 not in valores:
    print('O valor 5 não foi digitado')
print('-='*20)
print('FIM DO PROGRAMA')
