#Ler um preço do produto e mostrar o valor com 5% de desconto

valor = float(input('Valor do produto: R$'))

#descobrindo e mostrando a equação
print(f'O seu produto com 5% de desconto fica no valor de R${valor - (valor * 5 / 100):.2f}')