#PROGRAMA PRINCIPAL
#from moeda import metade,dobro, aumentar #caso eu queira importar algumas funções
from ex112.utilidadescev import moedas
from ex112.utilidadescev import dados
p = dados.leiaDinheiro('Digite o preço: R$')
moedas.resumo(p, 20, 12)
