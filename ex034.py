salario = float(input('Qual é o sálario do funcionário? R$'))
if salario > 1250:
    novo = salario * 1.10
else:
    novo = salario * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))