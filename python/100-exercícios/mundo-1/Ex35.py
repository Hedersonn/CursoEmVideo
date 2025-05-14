#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

comprimento1 = float(input('Primeira Reta: '))
comprimento2 = float(input('Segunda Reta: '))
comprimento3 = float(input('Terceira Reta: '))

if comprimento1 + comprimento2 > comprimento3 and comprimento2 + comprimento3 > comprimento1 and comprimento1 + comprimento3 > comprimento2:
    print(f'Suas medidas formam um triângulo.')
else:
    print('Suas medidas não formam um triângulo.')