'''Aula de manipulação de textos'''

'''--Fatiamento--

'''
frase = 'Curso em vídeo Python'
'''print(frase [9])'''

'''---Análise---
°Len = Conta a quantidade total de caracteres
°frase.count = conta quantas vezes aparece no texto o que está entre aspas 
°frase.find = Mostra em qual posiçao começa o caractere
°Infrase = mostra se o que está na frase é verdadeiro ou falso
'''

'''print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print('em' in frase)'''

'''---Transformação=--
Replace = Ele substitui letras ou palavras 
UPPER = Deixa o texto todo em maiúsculo 
lower = Deixa o texto todo em minuscúlo
Capitalize = Deixa a primeira letra da frase em Maiuscúla... ex: 'Curso em vídeo python'
title = A cada espaço ele transforma a letra em maiuscúla;;;ex: 'Curso Em Video Python'
strip = Remove todos os espaços inúteis
lstrip = Remove todos os espaços inúteis á esquerda
rstrip = Remove todos os espaços inúteis á direita 
'''
'''print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase.capitalize())'''

print(frase.split())
'-'.join(frase)