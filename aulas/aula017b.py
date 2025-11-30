# Posições e Estruturas de Repetição
valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))

for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')