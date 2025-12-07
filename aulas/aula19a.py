#APREDENDO DICIONÁRIOS EM PYTHON

filmes = {'titulo': 'starwars',
          'ano': 1977,
          'diretor': 'George Lucas'}
print(filmes['titulo'])
print(filmes['ano'])
print(filmes['diretor'])
print(filmes.values()) #MOSTRA TODOS OS VALORES NO DICIONÁRIO
print(filmes.keys())  #MOSTRA AS PALAVRAS-CHAVES
print(filmes.items()) #MOSTRA VALORES E DADOS JUNTOS

#USANDO ESTRUTURA DE REPETIÇÃO COM DICIONÁRIO
for key, value in filmes.items():
    print(f'O {key} é {value}')
