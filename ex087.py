matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = somacolun = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if coluna == 2:
            somacolun += matriz[linha][coluna]
print('=-' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=-' * 30)
print(f'Os valores pares digitados foram: {pares}')
print(f'A soma dos valores da terceira coluna é: {somacolun}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
