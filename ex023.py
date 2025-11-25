import math
numero = int(input('Digite um número de 0 a 9999:'))
unidades = math.trunc(numero)
decimal = numero % 10
centena = numero // 100
dezena = numero // 10 % 10
print('Unidade:{}'.format(unidades))
print('Decimal:{}'.format(decimal))
print('Centena:{} '.format(centena))
print('Dezena :{}'.format(dezena))