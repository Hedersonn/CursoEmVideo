# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint
from time import sleep

#Contador
vitorias = 0

#Loop
while True:
    computador = randint(0, 10)
    escolha = str(input("Escolha PAR ou IMPAR: ")) .upper() .strip()
    numero = int(input("Digite um numero de 0 a 10: "))
    soma = computador + numero

    print("Processando...")
    print("=" * 20)
    sleep(3)

    print(f"Voce escolheu {escolha} e eu fiquei com {"PAR" if escolha == 'IMPAR' else 'IMPAR'}")
    print(f"Computador > {computador}\nJogador > {numero}\nNumero gerado: {soma} ({'Par' if soma % 2 == 0 else 'Impar'})")

    print("=" * 20)
    print("Aguarde..")
    sleep(1)

    if escolha == "PAR":
        if soma % 2 == 0:
            print("Voce ganhou!")
            vitorias += 1
        else:
            print("Voce perdeu")
            break
    elif escolha == "IMPAR":
        if soma % 2 == 0:
            print("Voce perdeu")
            break
        else:
            print("Voce ganhou!!")
            vitorias += 1
    else:
        print("Invalido, digite novamente")

print(f"Vitorias: {vitorias}")



    