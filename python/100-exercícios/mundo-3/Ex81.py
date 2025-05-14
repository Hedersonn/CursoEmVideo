#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

from time import sleep

# Valores

numeros = []
continuar = ""

#Loop

while True:
    numeros.append(int(input("Digite um número:")))
    continuar = str(input("Quer continuar? > S|N < : "))[0]
    if continuar in "Nn":
        print("Fechando o programa...")
        sleep(2)
        break
    cont_numero += 1

# Valores finais

print(f"Você digitou {len(numeros)} número{'s' if len(numeros) > 1 else ''}")
print(f"Sua lista > {sorted(numeros, reverse=True)}")
if 5 in numeros:
    print(f"O número 5 existe na lista.")
else:
    print("O número 5 não está na lista.")