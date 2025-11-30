# Análise de dados do grupo
total = totalh = totm20 =  0
print('=' * 40)
print('          CADASTRO DE PESSOAS')
print('=' * 40)
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        total += 1
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {totalh} homens cadastrados')
print(f'Total de mulheres com menos de 20 anos: {totm20}')