n = cont = soma = maior = menor = media = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print(f'Você digitou {cont} valores. O maior entre eles é {maior} e o menor é {menor}.\n'
      f'A soma desses valores é de {soma}, e a média é de {media:.2f}.')
