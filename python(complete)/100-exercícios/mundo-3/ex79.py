#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente


# Valores

numeros = []
continuar = ""

# Loop

while continuar != "N":
   novo_numero = int(input("Digite um número: "))
   if novo_numero in numeros:
        print("Não foi possível adicionar o número. Pois já é existente.")
   else:
       print("Número adicionado!")
       numeros.append(novo_numero)

   continuar = str(input("Deseja continuar? > S|N < ")) .upper() .strip()[0]


# Valores finais

print("Lista".center(20, '='))
print(sorted(numeros))