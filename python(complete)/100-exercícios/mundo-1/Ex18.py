#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo:'))

radiano = radians(angulo)#Mudar de Grau para Radiano

print(f'O seno do ângulo {angulo} é {sin(radiano):.2f}')#mostrar o seno
print(f'O cosseno é {cos(radiano):.2f}')#mostrar o cosseno
print(f'A tangente é {tan(radiano):.2f}')#mostrar a tangente