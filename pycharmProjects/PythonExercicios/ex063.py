print('~'*30)
print('Sequência de Fibonacci')
print('~'*30)
termos = int(input('Quantos termos deseja ver? '))
t1 = 0
t2 = 1
t3 = 0
seq = 3
print(f'{t1} ⇢ {t2}', end='')
while seq <= termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    seq += 1
    print(f' ⇢ {t3}', end='')
print('\n')
print('-='*15)
