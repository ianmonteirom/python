n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é maior.')
#if n1 < n2:
    #print('O PRIMEIRO valor é menor.')
#elif n2 < n1:
    #print(f'{n2} é o menor valor.')
elif n1 == n2:
    print('Ambos possuem valor igual.')
