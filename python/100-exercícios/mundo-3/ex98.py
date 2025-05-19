#  Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizadap

from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    print("=" * 40)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=" - ", flush=True)
            sleep(0.5)
    else:
        passo = -passo
        for c in range(inicio, fim - 1, passo):
            print(c, end=" - ", flush=True)
            sleep(0.5)

    print("Fim!")

contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input("Início da contagem: "))
fim = int(input("Fim da contagem: "))
passo = int(input("Intervalo da contagem: "))
contador(inicio, fim, passo)