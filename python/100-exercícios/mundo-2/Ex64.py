#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


#Valores
numero = int(input("Digite um numero inteiro (999 cancela)\n> "))

#Contadores
quantidade = soma = 0

#Loop
while numero != 999:
    quantidade += 1
    soma += numero
    numero = int(input("Digite um numero inteiro (999 cancela)\n> "))
print(f"Numeros Digitados: {quantidade}\nSoma entre eles: {soma}")