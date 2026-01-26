def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
'''Acima o X é considerado uma variável/escopo local, porque só vai funcionar na função'''

#ESCOPO DE VARIÁVEIS
#Programa Principal
'''Abaixo o N será considerado uma variável/escopo global, porque pode ser usado no programa principal e na função '''
n = 2
print(f'No programa principal, n vale {n}')
teste()