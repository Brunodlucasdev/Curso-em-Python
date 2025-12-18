#UNINDO DICIONÁRIOS E LISTAS
galera = []
pessoas = {}
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 40)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade das pessoas é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) As pessoas cadastradas acima da média são: ')
for p in galera:
    if p['idade'] > media:
        print(f'     ')
        for key, value in p.items():
            print(f'{key} = {value}; ',end='')
        print()
print('<<<<     ENCERRADO       >>>>')