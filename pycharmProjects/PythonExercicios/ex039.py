from datetime import date
ano = date.today().year
s = int(input('Informe seu sexo abaixo \n'
              '[ 1 ] Para MASCULINO\n'
              '[ 2 ] para FEMININO\n'
              'Digite uma opção: '))
if s == 1:
    a = int(input('Digite seu ano de nascimento: '))
    if ano - a < 18:
        print(f'Ainda não está na hora de se alistar, você faz ou já fez {ano-a} anos este ano.\n'
          f'Ainda faltam {18-(ano-a)} anos para seu alistamento.'
          f'\n{a+18} é o ano em que você faz 18 anos.')
    elif ano - a == 18:
        print('Agora é a hora de se alistar, pois você completou ou completa 18 anos este ano.')
    elif ano - a > 18:
        print(f'Já passou do tempo de se alistar. Você faz ou já fez {ano-a} anos este ano\n'
          f'Já se passaram {(ano-a)-18} anos desde o ano do seu alistamento.\n'
          f'{a+18} foi o ano em que completou 18 anos.')
elif s == 2:
    print('Você não precisa fazer o alistamento militar obrigatório.')
