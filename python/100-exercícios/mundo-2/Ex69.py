#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

from time import sleep

# Contadores
maioridade = 0
homens = 0
mulheres = 0

# Loop
while True:
    print("=" * 20)
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo [M/F]: ").strip().upper()
    continuar = input("Quer continuar? [S / N] ") .strip() .upper()
    if idade > 18:
            maioridade += 1
    if sexo == "M": 
            homens += 1
    if sexo == "F" and idade < 20:
            mulheres += 1
    if continuar == "N":
        print("Ok, Encerrando programa.")
        sleep(1)
        break

print("=" * 30)
print(f"Pessoas maiores de 18 anos: {maioridade}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres com menos de 20 anos: {mulheres}")
