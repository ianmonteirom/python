print('-='*20)
print('{:^40}'.format('BANCO'))
print('-='*20)
cont50 = cont20 = cont10 = cont1 = 0
dinheiro = int(input('Qual o valor que deseja sacar? R$'))
while True:
    if dinheiro >= 50:
        while dinheiro >= 50:
            cont50 += 1
            dinheiro -= 50
        print(f'Total de {cont50} cédulas de R$50')
    if dinheiro >= 20:
        while dinheiro >= 20:
            cont20 += 1
            dinheiro -= 20
        print(f'Total de {cont20} cédulas de R$20')
    if dinheiro >= 10:
        while dinheiro >= 10:
            cont10 += 1
            dinheiro -= 10
        print(f'Total de {cont10} cédulas de R$10')
    if dinheiro >= 1:
        while dinheiro >= 1:
            cont1 += 1
            dinheiro -= 1
        print(f'Total de {cont1} cédulas de R$1')
    if dinheiro == 0:
        break
print('-='*20)
print('Volte sempre ao nosso banco!')
