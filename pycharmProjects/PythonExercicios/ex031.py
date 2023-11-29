dis = float(input('Qual a distância da sua viagem? KM: '))
if dis <= 200:
    print(f'Valor a pagar: R${dis*0.50:.2f}')
else:
    print(f'Valor a pagar: R${dis*0.45:.2f}.')

