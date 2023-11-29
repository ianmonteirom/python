r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('É POSSÍVEL formar um triângulo com esses segmentos ', end='')
    if r1 == r2 == r3:
        print('e será um triângulo EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('e será um triângulo ESCALENO.')
    else:
        print('e será um triângulo ISÓSCELES.')
else:
    print('Não é possível formar um triângulo com essas retas.')

