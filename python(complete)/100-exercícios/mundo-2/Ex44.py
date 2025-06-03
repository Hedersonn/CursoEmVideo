# #Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

#Valores
valor = float(input('Valor do produto: R$ '))

print('*' * 45)
pagamento = int(input('''[ 1 ] À vista dinheiro/cheque (desconto 10%)
[ 2 ] À vista no cartão (desconto 5%)
[ 3 ] 2X no cartão (normal)
[ 4 ] 3X ou mais (juros 20%)
> '''))
print('*' * 45)

#Condições
if pagamento == 1:
    desconto = valor * 0.1
    valor_total = valor - desconto
    print(f'''Desconto: R${desconto:.2f}
Juros: R$0
Pagamento final: R${valor_total:.2f}''')
elif pagamento == 2:
    desconto = valor * 0.05
    valor_total = valor - desconto
    print(f'''Desconto: R${desconto:.2f}
Juros: R$0
Pagamento final: R${valor_total:.2f}''')
elif pagamento == 3:
    print(f'''Desconto: R$0
Juros: R$0
Pagamento final : R${valor:.2f}''')
elif pagamento == 4:
    juros = valor * 0.2
    valor_total = valor + juros
    print(f'''Desconto: R$0
Juros: R${juros:.2f}
Pagamento final: R${valor_total:.2f}''')
else:
    print('Número inválido!')
