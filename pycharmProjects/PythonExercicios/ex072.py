extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = -1
while True:
    while num not in range(0, 21):
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}')
    num = -1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Você quer continuar? [S/N] ')).lower().strip()
    if continuar == 'n':
        break
print('--------FIM DO PROGRAMA--------')
