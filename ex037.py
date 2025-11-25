num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opçao: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida. Tente novamente!')