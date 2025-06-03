#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Valor

jogadores = []

# Loop

while True:
    jogador = {
        "jogador": "",
        "gols": [],
        "total": 0
    }

# Mostrar jogadores

    jogador["jogador"] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['jogador']} jogou? "))

    for i in range(partidas):
        jogador["gols"].append(int(input(f"Gols na partida {i + 1}: ")))

    jogador["total"] = sum(jogador["gols"])
    jogadores.append(jogador.copy())

    while True:
        continuar = input("Quer continuar? S|N: ").strip().upper()
        if continuar in "SN":
            break
        print("Erro! Digite apenas S ou N.")
    
    if continuar == "N":
        break

print("\n" + " DADOS DOS JOGADORES ".center(45, "-"))

print(f"{'ID':<5}{'Nome':<15}{'Gols':<15}{'Total':<5}")
for i, j in enumerate(jogadores):
    print(f"{i:<5}{j['jogador']:<15}{str(j['gols']):<15}{j['total']:<5}")

# Mostrar detalhes individuais
while True:
    print("-" * 45)
    escolha = int(input("Digite o ID para ver detalhes (999 para sair): "))
    
    if escolha == 999:
        break
    
    if 0 <= escolha < len(jogadores):
        jogador = jogadores[escolha]
        print(f"-- LEVANTAMENTO DO JOGADOR {jogador['jogador']} --")
        for i, g in enumerate(jogador["gols"]):
            print(f"  No jogo {i + 1} fez {g} gol{'s' if g != 1 else ''}.")
    else:
        print("ERRO! Não existe jogador com esse ID.")


            
    

