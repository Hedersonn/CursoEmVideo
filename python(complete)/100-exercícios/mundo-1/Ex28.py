#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

#Valores
computador = randint(0, 5)

print('><' * 15)

print('Digite um número de 0 a 5: ')
jogador = int(input(''))

#Condições
print(f'Eu escolhi {computador}')
print('><' * 15)
if jogador == computador:
    print('Você ganhou!!')
else:
    print('Você perdeu!!!!')
print('__' * 15)