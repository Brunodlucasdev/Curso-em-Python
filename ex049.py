print('=' * 20, end= ' ' )
print('Tabuada v2.0', end= ' ')
print('=' * 20 )
num = int(input('Digite um valor para ver a tabuada:'))
for c in range(1, 11):
    print( '{} x {:2} = {}'.format(num, c , num * c )) 