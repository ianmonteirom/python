frase = str(input('Digite uma frase: ')).strip().lower().split()
junta = ''.join(frase)
print(f'A frase normal é {junta}, e invertida fica {junta[::-1]}')
if junta == junta[::-1]:
    print('Essa frase É um PALÍNDROMO.')
else:
    print('Essa frase NÃO É um palíndromo.')


