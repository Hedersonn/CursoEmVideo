# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).strip().upper()

print(f'Quantidade de A: {frase.count('A')}')
print(f'Primeira posição: {frase.find('A') + 1}')
print(f'Última posição: {frase.rfind('A') + 1}')