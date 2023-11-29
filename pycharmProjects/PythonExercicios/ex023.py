num = int(input('Digite um número de 0 a 9999: '))
unidade = num//1%10
dezena = num//10%10
centena = num//100%10
milhar = num//1000%10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))



