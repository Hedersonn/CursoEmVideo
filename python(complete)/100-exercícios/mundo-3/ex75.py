#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

#Valores

#Contadores

contador = 0

numeros = (
    int(input("Digite um numero: ")),
    int(input("Digite outro numero: ")),
    int(input("Digite outro numero: ")),
    int(input("Digite outro numero: "))
    )


#Valores Finais

print(f"O número 9 apareceu {numeros.count(9)} Vez{'es' if numeros.count(9) > 1 else ''}")
if 3 in numeros:
    print(f"O número 3 foi encontrado na posição {numeros.index(3) + 1}")
else:
    print("O número 3 não está na tupla.")
print("Os números pares são: " ,end="")
for numero in numeros:

    if numero % 2 == 0:
        contador += 1
        print(numero, end=" ")
if contador == 0:
    print("Nenhum")
        



