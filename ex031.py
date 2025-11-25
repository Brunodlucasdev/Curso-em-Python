viagem = float(input('Qual é a distância da sua viagem ?'))
print('Você está prestes a começar uma viagem de {}km!'.format(viagem))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))