#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 


# Valores
#  
numeros = [int(input("Digite um valor: ")),
           int(input("Digite outro valor: ")),
           int(input("Digite outro valor: ")),
           int(input("Digite outro valor: ")),
           int(input("Digite outro valor: "))
           ]

# Contadores

maior = max(numeros)
menor = min(numeros)


#Valores finais

print(f"Maior número: {maior} está na posição {numeros.index(maior) + 1}")
print(f"Menor número: {menor} está na posição {numeros.index(menor) + 1}")
