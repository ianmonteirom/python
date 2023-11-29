nome = str(input('Digite seu nome completo: ')).title().strip()
n = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(n[0], n[-1]))

#print('Seu primeiro nome é {}'.format(nome.split()[0]))

#ultimonome = nome[nome.rfind(' '):]
#print('Seu último nome é {}'.format(ultimonome))
