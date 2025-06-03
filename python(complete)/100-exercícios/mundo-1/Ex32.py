#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar


#Valores
ano = int(input('Digite um ano: '))

#Condições
if calendar.isleap(ano):
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')