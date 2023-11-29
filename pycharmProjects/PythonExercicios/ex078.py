valores = []
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {v+1}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} e ele está na {valores.index(max(valores))+1}ª posição')
print(f'O menor valor digitado foi {min(valores)} e ele está na {valores.index(min(valores))+1}ª posição')
