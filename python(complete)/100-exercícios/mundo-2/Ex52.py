# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Valores
numero = int(input('Digite um número inteiro: '))

contador = 0
#Loop
for i in range (1, numero + 1):
    if numero % i == 0:
        contador += 1
if contador == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!\n Ele foi divisível por {contador} números')