p = float(input('Digite o preço do produto: R$'))
print('As formas de pagamento são:\n[ 1 ]: À vista com dinheiro/cheque (10% de desconto)\n[ 2 ]: À vista no cartão (5% de desconto)'
      '\n[ 3 ]: em até 2x no cartão (Sem desconto)\n[ 4 ]: 3x ou mais (20% de juros)')
f = int(input('Digite a forma de pagamento (1, 2, 3, 4): '))
if f == 1:
    print(f'Você escolheu o pagamento à vista com dinheiro. Total a pagar com 10% de desconto: R${p-(p*10/100):.2f}.')
elif f == 2:
    print(f'Você escolheu o pagamento à vista no cartão. Total a pagar com 5% de desconto: R${p-(p*5/100):.2f}.')
elif f == 3:
    print(f'Você escolheu o pagamento em até 2x no cartão. Total a pagar: 2x de R${p/2:.2f}.')
elif f == 4:
    x = int(input('Você escolheu o pagamento 3x ou mais no cartão. Escolha as prestações mensais em até 10x: '))
    if x <= 10:
        t = p/x
        j = (p/x)*20/100
        print(f'Total a pagar por mês: {x}x de R${t+j:.2f}')
    elif x > 10:
        print('Escolha as prestações mensais SOMENTE ATÉ 10x!')






