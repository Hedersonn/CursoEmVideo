#Ler um número e mostrar o dobro, triplo e sua raiz

from math import sqrt

numero = int(input('Digite um número: '))

print(f'Dobro: {numero * 2}')
print(f'Triplo: {numero * 3}')
print(f'Raiz: {sqrt(numero):.1f}')
