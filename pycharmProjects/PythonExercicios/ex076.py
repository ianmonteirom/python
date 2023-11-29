produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('--'*21)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*21)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    elif item % 2 != 0:
        print(f'R${produtos[item]:7.2f}')
print('--'*21)

'''print(f'{produtos[0]}...........................R$   {produtos[1]:.2f}')
print(f'{produtos[2]}........................R$   {produtos[3]:.2f}')
print(f'{produtos[4]}.........................R$  {produtos[5]:.2f}')
print(f'{produtos[6]}..........................R$  {produtos[7]:.2f}')
print(f'{produtos[8]}....................R$   {produtos[9]:.2f}')
print(f'{produtos[10]}........................R$   {produtos[11]:.2f}')
print(f'{produtos[12]}.........................R$ {produtos[13]:.2f}')
print(f'{produtos[14]}.........................R$  {produtos[15]:.2f}')
print(f'{produtos[16]}...........................R$  {produtos[17]:.2f}')
print('--'*21)'''

