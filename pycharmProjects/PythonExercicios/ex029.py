vel = float(input('Qual é a velocidade do carro? KM/H'))
if vel <=80.0:
    print('Tudo certo, você está dentro do limite de velocidade.')
else:
    print('Você foi multado por estar acima do limite de velocidade!')
    multa = (vel-80)*7
    print(f'Valor a pagar da multa: R${multa:.2f}. (Cada KM acima de 80KM/H adiciona R$7.00 a multa) ')#.format(multa))
