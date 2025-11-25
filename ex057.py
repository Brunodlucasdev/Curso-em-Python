sexo = str(input('Qual o seu sexo? [M/F]')).upper().strip()[0]
while sexo not in 'MmFf' :
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F]')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))