# VARIAÇÕES COMPOSTAS EM LISTAS
teste = list()
teste.append('Bruno de Lucas')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)