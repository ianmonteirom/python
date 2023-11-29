c = m = 0
campeao = str(input('Digite o nome do campeão: ')).strip().title()
while True:
    print('-='*30)
    conta = float(input(f'Digite a maestria da {c+1}ª conta: '))
    c += 1
    m += conta
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja digitar mais contas? [S/N] '))
    if continuar == 'n':
        break
print(f'Maestria total de {campeao}: {m:.3f}')
