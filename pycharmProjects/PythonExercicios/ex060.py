'''from math import factorial
num = int(input('Digite um número: '))
seq = num
f = 1
while seq > 0:
    print(f'{seq}', end='')
    print(' x ' if seq > 1 else ' = ', end='')
    f *= seq
    seq -= 1
print(f'{f}.')
#print(f'{factorial(num)}.')'''

# fazer com o for
num = int(input('Digite um número inteiro: '))
f = 1
for c in range(num, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}.')