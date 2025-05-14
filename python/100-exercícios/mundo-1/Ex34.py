# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#Valores
salario = float(input('Seu salário: '))

if salario > 1250:
    aumento = salario * 0.1 + salario
else:
    aumento = salario * 0.15 + salario
print(f'O seu salário de R${salario:.2f} passou a ser de R${aumento:.2f}')
