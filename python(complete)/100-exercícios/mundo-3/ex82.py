# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

from time import sleep

# Valores
numeros = []
pares = []
impares = []

#Loops

while True:
    numero = int(input("Digite um números: "))
    continuar = str(input("Quer continuar? > S|N < : "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    if continuar in "Nn":
        print("Fechando o programa...")
        sleep(1.5)
        break

print(f"Lista completa: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")