#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

#Cores
green = '\033[32m'
yellow = '\033[33m'
red = '\033[31m'
clear = '\033[m'

#Valores
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

#Condições
if media < 5.0:
    print(red + f' MEDIA DE {media:.1f}, REPROVADO!' + clear)
elif media < 7.0:
    print(yellow + f'MEDIA DE {media:.1f}, RECUPERAÇÃO' + clear)
else:
    print(green + f'MEDIA DE {media:.1f}, APROVADO' + clear)
