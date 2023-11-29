import random

jogs = []
modo = int(input('Quantos jogadores vão jogar? '))
times = int(modo/2)
for c in range(1, modo+1):
    jogs.append(str(input(f'{c}o Jogador: ')).title().strip())
print(f'Jogadores: {jogs}')
random.shuffle(jogs)
time1 = len(jogs)/2
print('----- TIME 1 ----')
for c in range(0, times):
    print(f'Jogador {c+1}: {jogs[c]}')
print('----- TIME 2 -----')
for c in range((times), len(jogs)):
    print(f'Jogador {c+1}: {jogs[c]}')
