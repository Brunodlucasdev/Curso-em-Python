#USANDO ESTRUTURAS DE REPETIÇAO DENTRO DO DICIONÁRIO E MAIS ESTRUTURA DE REPETIÇÕES
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for value in estado.values():
        print(value, end=' ')
    print()
