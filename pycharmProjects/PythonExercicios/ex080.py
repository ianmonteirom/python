valores = []
maior = menor = atual = 0
for v in range(0, 5):
    n = int(input('Digite um valor: '))
    atual += n
    if v == 0:
        maior = menor = n
    elif v != 0:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if n == maior:
        valores.append(n)
        print('Adicionado no final da lista...')
    elif n == menor:
        valores.insert(0, n)
        print('Adicionado na primeira posição da lista...')
    elif n > atual:
        valores.insert(1, n)
        print('Adicionado na segunda posição da lista...')
    elif n < max(valores):
        valores.insert(1, n)
        print('Adicionado na segunda posição da lista...')
    atual = 0
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')
