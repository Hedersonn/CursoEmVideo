# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras no total (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')) .strip()

print('Seu nome em: ')#Mostrar a introdução
print(f'Maiúsculas: {nome.upper()}')#Maiúscula
print(f'Minúsculas: {nome.lower()}')#Minúscula
print(f'Letras no total (menos espaços): {len(nome) - nome.count(' ')}')#Total de letras
print(f'Seu primeiro nome tem: { len(nome.split()[0])}')#Total de letras(primeiro nome)