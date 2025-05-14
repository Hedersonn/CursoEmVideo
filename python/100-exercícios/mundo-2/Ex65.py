#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


numero = int(input("Digite um numero: "))
continuar = str(input("Quer continuar? ")).upper() .strip()[0]
contador = 1
soma = maior = menor = numero

while continuar != "N":
    numero = int(input("Digite um numero: "))
    
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    
    continuar = str(input("Quer continuar? ")) .upper() .strip()[0]
    contador += 1
    soma += numero

media = soma / contador
print(f""" Maior valor: {maior}
Menor valor: {menor}
Soma entre todos os numeros: {soma}
Media entre eles: {media:.2f}""")