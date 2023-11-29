from math import hypot
a = float(input('Qual é o comprimento do cateto oposto? '))
b = float(input('Qual é o comprimento do cateto adjacente? '))
#c = a**2+b**2
#hyp = math.sqrt(c)
hyp = hypot(a, b)
print('O comprimento da hipotenusa deste triângulo retângulo é {:.2f}'.format(hyp))







