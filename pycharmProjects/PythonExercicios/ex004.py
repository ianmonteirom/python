cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'roxo': '\033[35m',
         'vermelho': '\033[31m'}
a = input('\033[31mDigite algo: ')
print(f'\033[36mO tipo primitivo de {a} é\033[1;4;35m', type(a))
print(f'\033[0;36m{a} só tem \033[1;4;35mespaços?\033[0;1;31m', a.isspace())
print(f'\033[0;36m{a} é um \033[1;4;35mnúmero?\033[0;1;31m', a.isnumeric())
print(f'\033[0;36m{a} é \033[1;4;35malfabético?\033[0;1;31m', a.isalpha())
print(f'\033[0;36m{a} é \033[1;4;35malfanumérico?\033[0;1;31m', a.isalnum())
print(f'\033[0;36m{a} está em \033[1;4;35mmaiúsculas?\033[0;1;31m', a.isupper())
print(f'\033[0;36m{a} está em \033[1;4;35mminúsculas?\033[0;1;31m', a.islower())
print(f'\033[0;36m{a} está \033[1;4;35mcapitalizada?\033[0;1;31m', a.istitle())








