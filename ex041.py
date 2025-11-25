import datetime
nasc = int(input('Ano de nascimento:'))
atual = datetime.date.today().year
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificaçãp: MIRIM')
elif idade <= 16:
    print('Classificaçãp: INFANTIL ')
elif  idade <= 19:
    print('Classificação: JÙNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classidicação: NASTER')