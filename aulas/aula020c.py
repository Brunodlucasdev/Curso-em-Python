#Empacotando Parâmteros
def contador(* num):
    print(f'Recebi os valores {num} e no total foram {len(num)} números')

#programa PRINCIPAL
contador(9, 5, 2)
contador(3, 4)
contador(0, 2, 3, 4, 5)
