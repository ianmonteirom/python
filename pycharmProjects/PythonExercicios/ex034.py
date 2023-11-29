s = float(input('Digite o valor do salário do funcionário: R$'))
if s <= 1250.00:
    print(f'O salário R${s:.2f} com um aumento de 15% (R${s*15/100:.2f}) passará a ser R${(s*15/100)+s:.2f}.')
else:
    print(f'O salário R${s:.2f} com um aumento de 10% (R${s*10/100:.2f}) passará a ser R${(s*10/100)+s:.2f}.')




