from random import choice
a1 = input('Qual o nome do primeiro aluno? ')
a2 = input('Qual o nome do segundo aluno? ')
a3 = input('Qual o nome do terceiro aluno? ')
a4 = input('Qual o nome do quarto aluno? ')
lista = [a1, a2, a3, a4]
aluno = choice(lista)
print('O aluno escolhido foi {}.'.format(aluno))





