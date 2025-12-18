#Desepacotanod Pârametros
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(2, 7)
soma(3, 5, 7)