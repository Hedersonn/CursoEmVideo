#Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Valor

matriz = []
pares = 0
terceira = 0

# Loop

for linha in range(1, 4):
    colunas = []
    for coluna in range (0, 3):
        valor = (int(input(f"Linha: {linha}\nColuna: {coluna + 1}\n >  ")))
        
        if valor % 2 == 0: # pares
            pares += valor
        if coluna == 2:
            terceira += valor

        colunas.append(valor)
    matriz.append(colunas)

print("=" * 40)
for lista in matriz:
    for numero in lista:
        print(f"[{numero:^5}]", end=" ")
    print()
print("=" * 40)

print(f"Soma dos pares: {pares}")
print(f"Soma da 3ª coluna: {terceira}")
print(f"Maior valor da 2ª linha: {max(matriz[1])}")
