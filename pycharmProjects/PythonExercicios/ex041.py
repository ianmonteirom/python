from datetime import date
n = int(input('Digite o seu ano de nascimento: '))
at = date.today().year
i = at - n
print(f'Idade: {i} anos.')
if i <= 9:
    print('Categoria do atleta: MIRIM (Até 9 anos).')
elif i <= 14:
    print('Categoria do atleta: INFANTIL (Até 14 anos).')
elif i <= 19:
    print('Categoria do atleta: JUNIOR (Até 19 anos).')
elif i <= 25:
    print('Categoria do atleta: SÊNIOR (Até 25 anos).')
else:
    print('Categoria do atleta: MASTER (Acima de 25 anos).')
