n = cont = soma = maior = menor = 0
continuar = ''
while continuar != 'n':
    if continuar != 'n':
        cont += 1
        n = int(input('Digite um número inteiro: '))
        continuar = str(input('Deseja digitar mais valores? [S/N]: ')).strip().lower()
        soma += n
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    while continuar != 's' and continuar != 'n':
        print('Digite uma opção válida!')
        continuar = str(input('Deseja digitar mais valores? [S/N]: ')).strip().lower()
if continuar == 'n':
    print(f'Você digitou {cont} valores, o maior entre eles é {maior} e o menor é {menor}. A média desses números é {soma/cont:.2f}.')
