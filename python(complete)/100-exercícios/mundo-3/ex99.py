# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*valores):
    maior = valores[0]

    for valor in valores:
        if valor > maior:
            maior = valor

    print(f"Foram informados {len(valores)} números, e o maior é {maior}")

numeros = []

while True:
    numero = int(input("Digite um número, 999 cancela: "))
    if numero == 999:
        break
    numeros.append(numero)

maior(*numeros)
