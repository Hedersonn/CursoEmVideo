#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


#Valores

extenso = (
    "Zero",
    "Um",
    "Dois",
    "Tres",
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dez",
    "Onze",
    "Doze",
    "Treze",
    "Quatorze",
    "Quinze",
    "Dezesseis",
    "Dezessete",
    "Dezoito",
    "Dezenove",
    "Vinte"
)

numero = int(input("Digite um numero para mostrar em extenso: "))

#Loop

while numero not in range(0, 21):
    numero = int(input("Numero invalido! Digite novamente: "))

print(f"O número {numero} por extenso é {extenso[numero]}")