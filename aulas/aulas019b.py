pessoas = {'nome': 'Bruno', 'sexo': 'Masculino', 'idade': 19}
pessoas['nome'] = 'Lucas' #SUBSTITUIÇÃO DE VALORES
pessoas['peso'] = 95.5 #ADICIONANDO VALOR
'''
#COMO FORMATAR DICIONÁRIO
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') 
'''
del pessoas['sexo'] #COMO APAGAR UM VALOR DENTRO DO DICIONÁRIO
for key, value in pessoas.items():
    print(f'{key} = {value}')
