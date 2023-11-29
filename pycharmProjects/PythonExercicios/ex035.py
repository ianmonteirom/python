r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r3 < r1+r2 and r2 < r1+r3 and r1 < r2+r3:
    print('É possível formar um triângulo com essas 3 retas.')
else:
    print('Não é possível formar um triângulo com essas 3 retas.')
