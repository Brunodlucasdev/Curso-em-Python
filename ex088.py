from random import randint
from time import sleep
lista = list()
jogos = list()
print('=-' * 20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('=-' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 0
while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-' * 5, f'SORTEANDO {quant} JOGOS', '=-' * 5)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1} {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
