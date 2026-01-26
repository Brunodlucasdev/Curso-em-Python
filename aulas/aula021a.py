#Parâmetros Opcionais

def somar(a=0,b=0,c=0):
    soma = a + b + c
    print(f'A soma vale {soma}')


somar(3, 2 , 5)
somar(4,6)
somar(c=3, a=2)

"""
def somar(a=0,b=0,c=0): 
    soma = a + b + c
    print(f'A soma vale {soma}')


somar(3, 2 , 5)
somar(4,6)
somar()
"""