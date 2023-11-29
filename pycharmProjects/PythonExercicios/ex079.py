valores = []
while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado! Não vou adicionar...')
    elif n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()
    if continuar == 'n':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(valores)}')
