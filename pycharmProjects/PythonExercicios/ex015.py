dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros o carro percorreu? '))
gasto = dias*60+km*0.15
print('Valor total a pagar pelo aluguel do veículo: R${:.2f}.'.format(gasto))

