valores = []
while True:
    n = valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar == 'n':
        break
pares = []
impares = []
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)
print('-='*20)
print(f'A lista completa é {valores}\n'
      f'A lista de pares é {pares}\n'
      f'A lista de ímpares é {impares}')
