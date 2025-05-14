# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

mais_barato = 0
gasto = 0
produtos_acima1000 = 0
nome = ""

while True:
    produto = input("Qual o nome do produto: ")
    preco = float(input(f"Qual o preco do(a) {produto}? "))
    gasto += preco
    continuar = " "
    while continuar not in "SsNn":
        continuar = input("Quer comprar mais produtos? [S / N] > ") .upper() .strip()
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        nome = produto
    if preco > 1000:
        produtos_acima1000 += 1
    if continuar == "N":
        print("Finalizando Compra..")
        break

print(f"""Produto mais barato: {nome}
Produtos acima de R$1000.00: {produtos_acima1000}
Total gasto na compra: {gasto:.2f}""")

    