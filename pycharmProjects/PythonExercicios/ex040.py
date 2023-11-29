n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5.0:
    print('Você foi reprovado. Estude mais.')
elif m >= 7.0:
    print('Parabéns, você foi aprovado!')
elif 5.0 <= m <= 6.9:
    print('Você ficou de recuperação, estude para a prova!')
print(f'Média: {m}.')
