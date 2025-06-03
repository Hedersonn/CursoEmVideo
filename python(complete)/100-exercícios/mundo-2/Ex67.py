#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#  O programa será interrompido quando o número solicitado for negativo. 

#Loop
while True:
    multiplo = 1
    numero = int(input("Digite um numero para sua tabuada: "))
    if numero < 0:
        break
    while multiplo < 11:
        multiplicacao = numero * multiplo
        print(f"{numero} x {multiplo:>2} = {multiplicacao}")
        multiplo += 1
        