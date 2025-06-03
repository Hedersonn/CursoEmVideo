#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


#Valores
numero = int(input('Digite um número: '))

#Condições
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')