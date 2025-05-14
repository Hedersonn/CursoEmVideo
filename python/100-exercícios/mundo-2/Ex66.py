#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#  que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

#Contadores
contador = soma = 0

#Loop
while True:
    numero = int(input("Digite um numero (999 para sair): "))

    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"Voce digitou {contador} numeros e a soma entre eles e {soma}")
    