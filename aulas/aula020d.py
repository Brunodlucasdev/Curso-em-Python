#Dobrando valores
def dobra(dobro):
    pos = 0
    while pos < len(dobro):
        dobro[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)
