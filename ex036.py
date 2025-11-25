print('-=-' * 20 )
print('Empréstimo Bancário')
print('-=-' * 20)
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento??'))
prestacao = casa  / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print('Empréstim pode ser CONCEDIDO ! ')
else:
    print('Empréstimo NEGADO!')