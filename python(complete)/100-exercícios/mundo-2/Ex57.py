# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Loop
sexo = str(input('Informe seu sexo [ M / F ]: ')) .upper() .strip()
while sexo not in  'MF':
    sexo = str(input('Sexo inválido! Digite novamente: ')).upper().strip()
print('Confirmado!')
