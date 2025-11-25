salario = float(input('Qual o valor do seu salário ?'))

valor = salario * 15//100
aumento = salario + valor

print('O valor reajustado do seu salário ficará assim R${:.0f}'.format(aumento))
