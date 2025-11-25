medida = float(input('Digite um valor em metros: '))

cm = medida * 100
mm = medida * 1000

print('A metragem que você colocou é essa {}m!\nO valor em centímetros é de: {:.0f}cm\nO valor em milímetros é de: {:.0f}mm'.format(medida,cm,mm))