#screva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print("Fibonacci".center(20, "_"))
print("")

#Valores
termos = int(input("Digite quantos termos quer: "))
termo1 = 0
termo2 = 1
contador = 2

print("(", end="")
print(termo1, "-", termo2, end= "")


while termos > contador:
    soma = termo1 + termo2
    print(f" - {soma}", end = "")
    termo1 = termo2
    termo2 = soma
    contador += 1
print(")")

