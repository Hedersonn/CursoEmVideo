#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

from time import sleep

# Valores

pessoas = []
pessoa = []
maior_peso = menor_peso = 0
pessoas_pesadas = []
pessoas_leves = []

# Loop

while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

    continuar = str(input("Deseja continuar? S|N > "))

    if continuar in "Nn":
        print("Encerrando o programa..")
        sleep(1)
        break

for p in pessoas:
    if p[1] == maior_peso:
        pessoas_pesadas.append(p[0])
    elif p[1] == menor_peso:
        pessoas_leves.append(p[0])


# Mostra de valores

print(f"Cadastros > {contador}")
print(f"Pessoas com maior peso > {maior_peso} < {pessoas_pesadas}")
print(f"Pessoas com menor peso > {menor_peso} < {pessoas_leves}")
print(pessoas)


