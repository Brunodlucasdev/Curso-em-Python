#PROGRAMA PRINCIPAL
#from moeda import metade,dobro, aumentar #caso eu queira importar algumas funções

import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10, True)}')
print(f'Reduzindo em 15% temos {moeda.diminuir(p,15, True)}')
