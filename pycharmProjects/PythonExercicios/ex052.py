n = int(input('Digite um número inteiro: '))
soma = 0
cont = 0
for p in range(1, n+1):
    r = n/p
    if n % p == 0:
        soma += 1
if soma == 1:
    print(f'O número {n} foi divisível somente {soma} vez, logo É primo.')
elif soma == 2:
    print(f'O número {n} foi divisível somente {soma} vezes, logo É primo.')
else:
    print(f'O número {n} foi divisível {soma} vezes, portanto NÃO É primo.')
