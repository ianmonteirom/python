from time import sleep
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
termos = int(input('Digite quantos termos deseja mostrar: '))
cont = 1
c = 0
pt = primeiro
reiniciar = True
continuar = 's'
while reiniciar:
    while cont <= termos:
        print(f'{pt}', ' ➝ ' if cont < termos else ' ➝ ...', end='')
        pt += razao
        cont += 1
        c += 1
    sleep(2)
    continuar = str(input('\nDeseja mostrar mais termos? [S/N]: ')).strip().lower()[0]
    if continuar == 's':
        reiniciar = True
        cont = 1
        termos = int(input('Quantos? '))
    elif continuar == 'n':
        reiniciar = False
    while continuar not in 'sn':
        print('Opção inválida!')
        continuar = str(input('Deseja mostrar mais termos? [S/N]')).strip().lower()[0]
        if continuar == 's':
            reiniciar = True
            cont = 1
            termos = int(input('Quantos? '))
        elif continuar == 'n':
            reiniciar = False
if not reiniciar:
    print('')
    print(f'Progressão finalizada com {c} termos mostrados.')
    print('FIM DO PROGRAMA')
    print('-=' * 10)
