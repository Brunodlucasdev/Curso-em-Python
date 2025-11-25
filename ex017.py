from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h1 = (hypot(co, ca))

print('Portanto o valor da hipotenusa é de: {:.2f}'.format(h1))