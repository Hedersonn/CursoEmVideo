# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando os 5 números...")
    sleep(3)

    for n in range(0, 5):
        numero = randint(0, 10)
        lista.append(numero)

        print(numero, end=" ", flush=True)
        sleep(0.75)

    print("Pronto!")



def somaPar(pares):
    soma = 0
    for numero in pares:
        if numero % 2 == 0:
            soma += numero
    print(f"A soma dos números pares de {pares} é {soma}")


numeros = []
sorteia(numeros)
somaPar(numeros)