#PROGRAMA PRINCIPAL
#from moeda import metade,dobro, aumentar #caso eu queira importar algumas funções
from ex111.utilidadescev import moedas

p = float(input('Digite o preço: R$'))
moedas.resumo(p, 20, 12)
