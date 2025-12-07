#Cadastro de Jogador de futebol
# Três maneiras de mostrar informações
jogador = dict()
partidas = list()
jogador['nome']  = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for n in range(0, total):
    partidas.append(int(input(f'  Quantos gols na partida {n}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-' * 40)
print(jogador)
print('=-' * 40)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value} ')
print('=-' * 40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, value in enumerate(jogador['gols']):
    print(f'   => Na partida {indice}, fez {value} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
