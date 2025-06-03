# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# from math import sqrt


# cateto_o = float(input('Cateto Oposto: '))
# cateto_a = float(input('Cateto Adjacente: '))
#
# equacao = cateto_o ** 2 + cateto_a ** 2
# hipotenusa = sqrt(equacao)
#
# print(f'A Hipotenusa do triângulo retângulo é de {hipotenusa:.2f} metros. ')

from math import hypot

cateto_o = float(input('Cateto Oposto: '))
cateto_a = float(input('Cateto Adjacente: '))

hipotenusa = hypot(cateto_o, cateto_a)

print(f'A hipotenusa entre os catetos deu {hipotenusa:.2f} Metros.')