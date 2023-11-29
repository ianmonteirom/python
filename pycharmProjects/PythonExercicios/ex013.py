n = float(input('Qual o salário do funcionário? R$'))
p = 0.15*n
v = n+p
print('Ao aumentar 15% do salário, o funcionário passará a ganhar R${:.2f} no total, com um aumento de R${:.2f}.'.format(v, p))

