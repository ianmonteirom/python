'''num = [1, 5, 6, 3, 9]
num[2] = 7
num.append(4)
num.sort(reverse=True)
num.insert(3, 0)
num.pop(3)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for pos, v in enumerate(valores):
    print(f'Encontrei {v} na posição {pos+1}')
