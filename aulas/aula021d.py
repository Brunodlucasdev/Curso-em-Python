# DIFERENCIADO ESCOPOS GLOBAIS E LOCAIS
"""
-> Toda variável declarada dentro da função é considerada escopo local
-> Se a variável for declarada no programa principal, ela é considerada escopo global
# Caso seja um escopo global, a variável pode ser usado no programa principal ou na função por exemplo
função [global] usada para alterar o valor que estiver na declarado no local
"""

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')