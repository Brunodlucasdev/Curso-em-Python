#Calcúlo de área de terreno
def area():
    areatot = largura * comprimento
    print(f'A área do terreno {largura}x{comprimento} é de {areatot}m²')



print(f'{'Controle de terrenos':^40}')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area()
