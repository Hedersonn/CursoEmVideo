#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maiorEscreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

#Valores

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

#Condições
if numero1 > numero2:
    print(f'O número {numero1} é maior que o {numero2}.')
elif numero2 > numero1:
    print(f'O número {numero2} é maior que o {numero1}.')
else:
    print('Os dois são iguais.')