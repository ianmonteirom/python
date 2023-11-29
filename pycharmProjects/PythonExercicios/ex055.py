maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior:.1f}KG e o menor peso é {menor:.1f}KG.')


'''p1 = float(input('Digite o primeiro peso (KG): '))
p2 = float(input('Digite o segundo peso (KG): '))
p3 = float(input('Digite o terceiro peso (KG): '))
p4 = float(input('Digite o quarto peso (KG): '))
p5 = float(input('Digite o quinto peso (KG): '))
lista = [p1, p2, p3, p4, p5]
for peso in lista:
    if peso > maior:
        maior = peso
for peso in lista:
    if peso < menor:
        menor = peso + 1000 - 1000
print(f'O maior peso é {maior:.1f}KG e o menor peso é {menor:.1f}KG.')'''
