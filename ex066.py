# Vários números com flag
soma = cont =  0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A quantidade de números digitados foi {cont} e a soma entre eles {soma}')