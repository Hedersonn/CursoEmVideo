#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# Valor

matriz = []

# Loop

for linha in range(1, 4):
    colunas = []
    for coluna in range (0, 3):
        colunas.append(int(input(f"Linha: {linha}\nColuna: {coluna + 1}\n >  ")))
    matriz.append(colunas)

for lista in matriz:
    for numero in lista:
        print(f"[{numero:^5}]", end=" ")
    print()
