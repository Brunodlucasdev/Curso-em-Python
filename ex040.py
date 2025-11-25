nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda note: '))
media = (nota1+nota2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
if media >= 6:
    print('O aluno está APROVADO.')
elif 5 <= media < 6.0:
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')