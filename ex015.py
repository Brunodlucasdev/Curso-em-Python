aluguel = int(input('Quantos dias alugados ?  '))
kilometros = float(input('Quantos Km rodados ?  '))
dias = aluguel * 60
km = kilometros * 0.15
total = dias + km
print('O total a pagar é de R${:.2f}'.format(total))
