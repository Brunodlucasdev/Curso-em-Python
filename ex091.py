from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for key, value in jogo.items():
    print(f'O {key} tirou {value} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-' * 38)
print('  == RANKING DOS JOGADORES ==  ')
for indice, value in enumerate(ranking):
    print(f'  O {indice+1}ª lugar: {value[0]} com {value[1]}.')
    sleep(1)