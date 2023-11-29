sexo = str(input('Digite seu sexo [M/F]: ')).lower()[0].strip()
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Sexo inválido! Digite seu sexo [M/F]: ')).strip().lower()[0]
print('Sexo salvo!')
