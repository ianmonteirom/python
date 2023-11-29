nome = str(input('Digite seu nome completo: ')).strip().title()
nomedividido = nome.split()
nomesemespaço = ''.join(nomedividido)
print('Seu nome com todas as letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome completo possui {} letras.'.format(len(nomesemespaço)))
print('Seu primeiro nome é {} e possui {} letras.'.format(nomedividido[0], len(nomedividido[0])))

