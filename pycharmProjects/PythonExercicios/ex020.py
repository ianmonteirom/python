from random import shuffle
a1 = str(input('Qual é o nome do primeiro aluno? '))
a2 = str(input('Qual é o nome do segundo aluno? '))
a3 = str(input('Qual é o nome do terceiro aluno? '))
a4 = str(input('Qual é o nome do quarto aluno? '))
lista = [a1, a2, a3, a4]
aluno = shuffle(lista)
print('A ordem dos alunos será ')
print(lista)






