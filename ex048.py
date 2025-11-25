soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        soma +=c
        cont += 1
print('As somas de todos os {} valors solicitados é {}'.format(cont,soma))
