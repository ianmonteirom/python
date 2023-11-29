primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(f'{termo} ➝ ', end='')
    termo += razao
    cont += 1
print('FIM')
