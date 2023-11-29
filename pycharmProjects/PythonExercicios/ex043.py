a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p/a**2
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} e está classificado como \033[31mAbaixo do Peso\033[m (Menor que 18.5).')
elif 18.5 <= imc <= 24.9:
    print(f'Seu IMC é de {imc:.2f} e está classificado como \033[31mPeso Ideal\033[m (Entre 18.5 a 25).')
elif 25 <= imc <= 29.9:
    print(f'Seu IMC é de {imc:.2f} e está classificado como \033[31mSobrepeso\033[m (Entre 25 a 30, Obesidade Grau 1).')
elif 30 <= imc <= 39.9:
    print(f'Seu IMC é de {imc:.2f} e está classificado como \033[31mObesidade\033[m (Entre 30 a 40, Obesidade Grau 2).')
elif imc >= 40:
    print(f'Seu IMC é de {imc:.2f} e está classificado como \033[31mObesidade Grave\033[m (Maior que 40, Obesidade Grau 3).')
