
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for n in range(0, total):
        partidas.append(int(input(f'   Quantos gols na partida {n}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for elemento in jogador.keys():
    print(f'{elemento:<15}', end='')
print()
print('=-' * 30)
for key, value in enumerate(time):
    print(f'{key:>3} ', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time)+1:
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, gols in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {gols} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE! >>')
