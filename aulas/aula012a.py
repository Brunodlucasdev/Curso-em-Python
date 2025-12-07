nome = str(input('Qual é o seu nome ?')).strip()
if nome == 'Bruno':
    print('Que nome bonito !!')
elif nome == 'João' or nome == 'Matheus' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))
