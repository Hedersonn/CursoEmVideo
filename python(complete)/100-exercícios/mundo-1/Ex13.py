#Salário com 15% de aumento

salario = float(input('Digite seu salário: R$'))

print(f'Você recebeu um aumento de 15%!!')
print(f'Seu salário que era de R${salario:.2f} passou a valer R${salario + (salario * 15 / 100)}')