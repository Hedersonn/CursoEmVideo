#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


#Import
from math import factorial


#Valores
numero = int(input('Digite um fatorial: '))

#Contadores
contador = numero
contar_fatorial = numero
print(f'{numero} ! = ',end='')

#Loop
while contar_fatorial > 0:
    print(f'{contar_fatorial} {'x' if contar_fatorial > 1 else '='} ',end='')
    contar_fatorial -= 1
    
print(factorial(numero))