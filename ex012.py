p = float(input('Qual o preço do produto? '))

s = p * 5//100
d = p - s

print("O valor do produto é de R${}"
      "\nO valor com 5% de desconto será de R${:.0f1}".format(p, d))