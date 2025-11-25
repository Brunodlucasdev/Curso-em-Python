while True:
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')