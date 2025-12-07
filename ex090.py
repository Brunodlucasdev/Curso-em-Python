aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['Média'] < 7:
    aluno['situação'] = 'Reprovado'
print('=' * 40)
for key, value in aluno.items():
    print(f'  -{key} é igual a {value}')