#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

#Valores
frase = str(input('Digite uma frase: '))
frase_tratada = frase .upper() .replace(' ', '')


#Loop/Condições
if frase_tratada == ''.join(reversed(frase_tratada)):
    print(f'A frase {frase} forma um palíndromo!')
else:
    print(f'A sua frase não forma um palíndromo!')