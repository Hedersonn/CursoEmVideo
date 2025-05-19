#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


# Valores

jogador = {}
gols = []

jogador["Nome"] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))

# Loop/ Valores finais

for i in range(partidas):
    gols.append(int(input(f"Gols na partida {i + 1}: ")))

jogador["Gols Por Partida"] = gols
jogador["Total de Gols"] = sum(gols)

print("\n--- DADOS DO JOGADOR ---")

for chave, valor in jogador.items():
    print(f"{chave}: {valor}")

print("\n--- DETALHAMENTO ---")

for i, g in enumerate(jogador["Gols Por Partida"]):
    print(f"Na partida {i + 1}, fez {g} gol(s).")
print(f"Total de gols no campeonato: {jogador['Total de Gols']}")

