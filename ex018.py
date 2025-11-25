from math import radians ,sin, cos, tan
angulo=  float(input('Digite um angulo:'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o seno: {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o cosseno: {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a tangente: {:.2f}'.format(angulo, tangente))
