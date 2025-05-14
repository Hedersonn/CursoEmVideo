#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint


#Valores
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior = max(numeros)
menor = min(numeros)

print(F"A tupla formada e {numeros}\nMenor Valor: {menor}\nMAior Valor: {maior}")



