#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

# Ler o número de cada jogador

jogadores = {}

for j in range(1, 5):
    jogadores[f"jogador{j}"] = randint(1, 6)
    print(f"O jogador {j} tirou o número {jogadores[f"jogador{j}"]}")
    sleep(1.2)

# Colocar em ordem e mostrar na tela

jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for posicao, jogador in enumerate(jogadores):
    print(f"{posicao + 1}º lugar: {jogador[0]} com {jogador[1]}")
