peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do peso')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de Peso normal')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso')
elif 30 <= imc < 35:
    print('Você está com Obesidade grau 1')
elif 35 <= imc < 40:
    print('Você está com Obesidade grau 2')
elif 40 <= imc > 40.1 :
    print('Você está com Obesidade grau 3')
