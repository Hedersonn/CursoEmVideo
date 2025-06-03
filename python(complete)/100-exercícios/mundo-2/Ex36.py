# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Valores
casa = float(input('Valor da casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Quantidade de anos: '))

mes = anos * 12
prestaçao = casa / mes
porcentagem = salario * 0.3

#Condiçôes
print(f'Seu salário é de R${salario:.2f}')


if prestaçao > porcentagem:
    print(f'Não é possível conceder o empréstimo com a prestação de R${prestaçao:.2f}')
elif prestaçao <= porcentagem:
    print(f'Você consegue pagar a prestação da casa de R${prestaçao:.2f}.')
