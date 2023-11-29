primeiro = int(input('Qual o primeiro elemento da PA?'))
razao = int(input('Qual a razão?'))
termo = (primeiro + (9) * razao) + razao
for i in range(primeiro, termo+1, razao):
    print(i, end= ' -> ')
print(':)')

