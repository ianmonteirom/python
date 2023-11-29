frase = str(input('Digite uma frase: ')).strip().lower()#.split()
#frase = ''.join(f)
print('Sua frase possui {} caracteres.'.format(len(frase)))
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.find('a')+1))
print('A letra "a" aparece pela última vez na posição {}.'.format(frase.rfind('a')+1))
print(frase)



