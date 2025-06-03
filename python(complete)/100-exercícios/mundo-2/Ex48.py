#Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

#Repetição
soma = 0
for numero in range(3, 500, 3):
    soma += numero
print(f'A soma de todos os números é: {soma}')

