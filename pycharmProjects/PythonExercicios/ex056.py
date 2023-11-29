i = 0
maisvelho = 0
menosde20 = 0
nmv = 0
m = 0
h = 0
pessoas = int(input('Quantas pessoas deseja analisar? '))
for info in range(1, pessoas+1):
    print(f'----- {info}ª PESSOA ----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    if sexo == 'm':
        h = h+1
        if idade > maisvelho:
            maisvelho = idade
            nmv = nome
    elif sexo == 'f':
        m = m+1
        if idade < 20:
            menosde20 = menosde20+1
    i = idade+i
media = i/pessoas
print('--'*20)
print(f'A média das idades desse grupo é de {media:.1f} anos.')
if h != 0:
    print(f'O homem mais velho se chama {nmv} e possui {maisvelho} anos.')
elif h == 0:
    print('Não há homens neste grupo.')
if m != 0:
    if menosde20 == 1:
        print(f'Apenas {menosde20} mulher possui menos de 20 anos.')
    elif menosde20 != 0:
        print(f'Ao todo, {menosde20} mulheres possuem menos de 20 anos.')
    elif menosde20 == 0:
        print('Não há mulheres com menos de 20 anos neste grupo.')
elif m == 0:
    print('Não há mulheres neste grupo.')
print('--'*20)
