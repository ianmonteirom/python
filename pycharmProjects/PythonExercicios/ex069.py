demaior = menosde20 = homem = mulher = 0
while True:
    print('-'*30)
    print('   CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).lower().strip()[0]
    if idade >= 18:
        demaior += 1
    if sexo == 'm':
        homem += 1
    elif sexo == 'f':
        mulher += 1
    if sexo == 'f' and idade < 20:
        menosde20 += 1
    print('-'*30)
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar == 'n':
        break
print('======== FIM DO PROGRAMA ========')
print(f'Total de pessoas com mais de 18 anos: {demaior}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {menosde20} mulheres com menos de 20 anos.')
