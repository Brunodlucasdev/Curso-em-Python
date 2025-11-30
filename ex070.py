# Estatísticas em produto
print('=' * 40)
print('LOJA SUPER BARATÃO')
print('=' * 40)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto:'))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')