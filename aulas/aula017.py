#Testando funções dentro das listas
num = [1,2,3,4,5]
num[2] = 8
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 24 in num:
    num.remove(24)
else:
    print('Não achei o número 24')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
