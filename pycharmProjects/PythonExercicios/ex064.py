n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número inteiro (Digite 999 para parar): '))
    soma += n
    cont += 1
print(f'Você digitou {cont-1} números e sua soma final foi {soma - 999}.')
