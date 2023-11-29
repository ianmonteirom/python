palavras = ('Monitor', 'Teclado', 'Controle', 'Mouse', 'Mesa', 'Garrafa', 'Caderno', 'Cadeira',
            'Celular', 'Luvas', 'Papeis', 'Ventilador', 'Armario', 'Parede', 'Teto')
for lista in palavras:
    print(f'\nNa palavra {lista.upper()} temos ', end='')
    for letras in lista:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
