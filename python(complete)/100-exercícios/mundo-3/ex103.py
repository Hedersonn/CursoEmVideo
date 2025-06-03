# : Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

#Ler os dados do jogador

def ficha(jogador="desconhecido", gols=0):
    print(f"O jogador {jogador} fez {gols} gol{'s' if gols > 1 else ''}")

# Programa Principal

nome = str(input("Nome do jogador:")).strip()
gol = str(input("Número de gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == "":
    ficha(gols=0)
else:
    ficha(nome, gol)
    