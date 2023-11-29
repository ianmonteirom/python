soma = 0
v = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        v = v+1
        soma += i
print(f'A soma de todos os {v} números ímpares múltiplos de 3 é {soma}.')
