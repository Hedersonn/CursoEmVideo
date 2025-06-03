#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from time import sleep
from random import randint

# Valores

escolha = int(input("Quantos jogos irá querer?\n > "))
jogos = []
jogo = []

# Loop

for _ in range(0, escolha):
    contador = 0

    while True:
        numero = randint(1, 60)

        if numero not in jogo:
            jogo.append(numero)
            jogo.sort()
            contador += 1
        if contador == 6:
            jogos.append(jogo[:])
            jogo.clear()
            break


# Valores finais

print("-=" * 10, "MEGA SENA", "=-" * 10, "\n")

for i, j in enumerate(jogos):
    print(f"{i + 1}º Jogo > {j}".center(50))
    sleep(1)

print("\n", " Boa sorte ".center(52, "="))