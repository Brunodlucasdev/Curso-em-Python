#Funções parte 2, Help.
#print(str.__doc__) PRINTANDO A INFORMAÇÃO
#help(print) INFORMAÇÕES SOBRE A FUNÇÃO ESPECÍFICA


def contador(i, f, p):
#DOCSTRINGS ABAIXO
    """ 
    -> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f:fim da contagem
    :param p:passo da contagem
    :return:sem retorno
    """
    c=i
    while c <= f:
        print(f'{c}', end='..')
        c +=p
    print('FIM!')
contador(2,10,2)
contador(7,99, 15)
contador(100,890,20)
help(contador)