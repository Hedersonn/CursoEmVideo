 # Crie um programa que leia o ano de nascimento de sete pessoas.
 # No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

#Contadores
menores = 0
maiores = 0

#Loop/Condições
for i in range(1, 8):
    ano = int(input(f'Ano de nascimento da {i}ª pessoa: '))
    idade = date.today().year - ano
    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f'Menores de idade: {menores}\nMaiores de idade: {maiores}')