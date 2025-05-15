#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Valores

numeros = [[], []]

#Loop

for cont in range (0, 7):
    numero = int(input("Número > "))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

# Valores finais

print(f"Pares > {sorted(numeros[0])}")
print(f"Ímpares > {sorted(numeros[1])}")