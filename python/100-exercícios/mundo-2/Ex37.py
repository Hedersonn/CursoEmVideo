#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

#Dados
numero = int(input('Digite um número inteiro: '))
modo_de_conversao = int(input('Digite [ 1 ] para binário\nDigite [ 2 ] para octal\nDigite [ 3 ] para hexadecimal\n'))

#Conversão
binario = bin(numero)
octal = oct(numero)
hexa = hex(numero)

#Condições
if modo_de_conversao == 1:
    print(f'Seu número ({numero}) convertido em Binário é: {binario[2:]}')
elif modo_de_conversao == 2:
    print(f'Seu número ({numero}) convertido em Octal é: {octal[2:]}')
elif modo_de_conversao == 3:
    print(f'Seu número ({numero}) convertido em Hexadecimal é: {hexa[2:]}')