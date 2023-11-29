pt = int(input('Digite o primeiro termo desta progressão aritmética: '))
r = int(input('Digite a razão: '))
pa = pt+(10-1) * r
print('A progressão aritmética é: ', end='')
for i in range(pt, pa+r, r):
    print(f'{i},', end='')
print('...')
