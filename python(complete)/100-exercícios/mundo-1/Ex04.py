# Leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo para as informações: ')

print(f'Tipo primitivo: {type(algo)}')
print(f'É um número? {algo.isnumeric()}')
print(f'É uma letra? {algo.isalpha()}')
print(f'Possui os dois ou um deles? {algo.isalnum()}')
print(f'São apenas espaços? {algo.isspace()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está captalizada? {algo.istitle()}')