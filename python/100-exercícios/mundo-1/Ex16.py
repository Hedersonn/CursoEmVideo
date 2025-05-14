#Mostrar Um número inteiro

from math import trunc

numero = float(input('Digite um número para descobrir sua porção inteira:\n>'))
print(f'O número {numero} inteiro da {trunc(numero)}')