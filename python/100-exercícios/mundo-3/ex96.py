# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# Função

def area(larg, comp):
    area = larg * comp
    print(f"A área de {larg:.1f} x {comp:.1f} = {area:.1f}")

# Valores

largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))

area(largura, comprimento)