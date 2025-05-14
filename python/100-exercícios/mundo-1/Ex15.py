# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KM foram rodados? '))
dias = int(input('Quantos dias usou? '))

print(f'Valores: ')
print(f'{dias} dias ficou no valor de: R${dias * 60:.2f}')
print(f'{km:.2f}km ficou no valor de: R${km * 0.15:.2f}')
print(f'O total a pagar será de: R$ {(km * 0.15) + (dias * 60):.2f}')