'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

c = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o seu salário: R$'))
a = int(input('Em quantos anos você pretende pagar? '))
pm = (c/a)/12
p = s*30/100
if pm > p:
    print(f'Infelizmente, você não pode financiar esta casa. o valor da prestação mensal (R${pm:.2f}) está acima de 30% do seu salário.')
elif p >= pm:
    print(f'Seu empréstimo foi aceito. O valor da prestação mensal é de R${pm:.2f} e 30% do seu salário é de R${p:.2f}.')
