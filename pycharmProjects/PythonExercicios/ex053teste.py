total = 0
contas = int(input('Quantas contas você quer somar a maestria? '))
campeao = str(input('Qual campeão quer somar a maestria? ')).strip().title()
print('')
for c in range(1, contas+1):
    conta = str(input(f'Digite o nome da {c}° conta: '))
    maestria = float(input('Digite a maestria dela: '))
    print('')
    total += maestria
print(f'Sua maestria total de {campeao} é de {total:.3f}.')
