def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem de aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa / 100 )
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: Qual o preço que se quer reajustar.
    :param taxa: Qual a porcentagem de redução.
    :param formato: Quer a saída formatada ou não ?
    :return: O valor reajustado, com ou sem formato.
    """
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    """
    -> Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: Qual o preço que se quer dobrar.
    :param formato: Quer a saída formatada ou não ?
    :return: O valor reajustado, com ou sem formato.
    """
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    """
    -> Calcula a metade de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: Qual o preço que se quer a metade.
    :param formato: Quer a saída formatada ou não ?
    :return: O valor reajustado, com ou sem formato.
    """
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Formata o valor do moeda para o real.
    :param preco: sem finalidade
    :param moeda: Adicionando o símbolo do real (R$)
    :return: O valor da moeda formatada e o preço formatado para a moeda real.
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')



def resumo(preco=0, taxaa= 10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)