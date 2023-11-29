from math import radians, sin, cos, tan
angulo = int(input('Qual é o valor do ângulo? '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O SENO de {:.2f} é {:.2f}.\nO COSSENO de {:.2f} é {:.2f}.\nA TANGENTE de {:.2f} é {:.2f}.'.format(angulo, sen, angulo, cos, angulo, tan))




