# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#  e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep

# Valores

sacar = int(input("Digite o valor a ser sacado (Apenas valores inteiros): "))
nota1 = nota10 = nota20 = nota50 = 0

# Loop

while sacar >= 50:
    nota50 += 1
    sacar -= 50

while sacar >= 20:
    nota20 += 1
    sacar -= 20

while sacar >= 10:
    nota10 += 1
    sacar -= 10

while sacar >= 1:
    nota1 += 1
    sacar -= 1


# Mostrar Resultados


sleep(1)
print("-" * 40)
print("Quantidade de celulas ".center(40, "="))
print("-" * 40)

print(f"R$ 50.00 > {nota50}".center(40))
print(f"R$ 20.00 > {nota20}".center(40))
print(f"R$ 10.00 > {nota10}".center(40))
print(f"R$ 01.00 > {nota1}".center(40))

print("-" * 40)
print("Processo concluído. Obrigado por utilizar o caixa eletrônico!")
sleep(2)








