#Cópia de listas
a = [2, 3, 4, 7]
#b = a (Dessa maneira acaba ocorrendo uma ligação nas listas)
#b= a[:] (Maneira correta para fazer uma cópia da lista
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')