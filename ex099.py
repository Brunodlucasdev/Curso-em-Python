#Encontrando o maior valor com função
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-' * 60)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(2, 5 , 6 ,7 , 7 , 8, 9)
maior(6, 9 , 0 , 34, 75, 86, 44)
maior(234, 675, 763, 643, 855, 753,262)
maior(8)
maior()
