#080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

# Valores

numeros = []

# Loop

for contador in range (0, 5):
    numero = int(input("Digite um número: ")) 
    if contador == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero <= numeros[posicao]:
                numeros.insert(posicao, numero)
                break
        posicao += 1


# Valor final

print(f"A lista de forma ordenada fica : {numeros}")