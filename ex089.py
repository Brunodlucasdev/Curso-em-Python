lista = list()
notas = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)

    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break