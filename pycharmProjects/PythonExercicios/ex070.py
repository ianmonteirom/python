print('-'*30)
print('             LOJA')
print('-'*30)
soma = acima = menor = cont = 0
nomemenor = ''
while True:
    nome = str(input('Nome do Produto: ')).title()
    preco = float(input('Preço: R$'))
    soma += preco
    cont += 1
    if preco > 1000:
        acima += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomemenor = nome
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'Você comprou {cont} produtos e o total da compra foi de R${soma:.2f}')
print(f'Temos {acima} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemenor} que custa R${menor:.2f}')
