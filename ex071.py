print('=' * 30)
print('{:^30}'.format('BANCO D´LUCAS'))
print('='*30)
valor = float(input('Que valor que você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO D´LUCAS! Tenha um bom dia!')
