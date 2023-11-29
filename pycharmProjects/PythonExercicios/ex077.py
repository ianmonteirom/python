palavras = ('Monitor', 'Teclado', 'Controle', 'Mouse', 'Mesa', 'Garrafa', 'Caderno', 'Cadeira',
            'Celular', 'Luvas', 'Papeis', 'Ventilador', 'Armario', 'Parede', 'Teto')
for lista in palavras:
    print(f'\nNa palavra {lista.upper()} temos ', end='')
    for letra in lista:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

