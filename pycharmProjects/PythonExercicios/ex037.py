'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
 escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''

n = int(input('Digite um número inteiro: '))
print('Digite uma opção para conversão:\n'
      '[ 1 ] para BINÁRIO\n'
      '[ 2 ] para OCTAL\n'
      '[ 3 ] para HEXADECIMAL')
e = int(input('Digite sua escolha: '))
if e == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}.')
elif e == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}.')
elif e == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}.')
else:
    print('Opção inválida!')
