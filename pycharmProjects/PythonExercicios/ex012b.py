produto = float(input('Qual é o preço do produto? R$'))
vista = produto-(produto*10/100)
parcelado = produto-(produto*7/100)
print('O valor do seu produto que inicialmente é de R${} passará a valer R${} á vista com 10% de desconto, e R${} com 7% de desconto caso parcelado.'.format(produto, vista, parcelado))

