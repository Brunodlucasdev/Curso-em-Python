# Sequência de Fibonacci v1.0
print('-'*36)
print('Sequência de Fibonacci')
print('-'*36)
n = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('-'*36)
print('{} -> {} '.format(termo1, termo2), end='')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('\nA sequência foi finalizada com {} termos mostrados.'.format(n))
