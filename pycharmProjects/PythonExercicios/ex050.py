soma = 0
cont = 0
par = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° número inteiro: '))
    if n % 2 == 0:
        par = n
        cont += 1
        soma += n
if cont == 0:
    print('Você não digitou nenhum número par.')
if cont == 1:
    print(f'A soma do número par informado ({par}) é igual a {soma} (Ele mesmo).')
if cont >= 2:
    print(f'A soma dos {cont} números pares que você digitou é {soma}.')
