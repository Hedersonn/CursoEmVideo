#Crie um mini-sistema que utilize a Ajuda Interativa do Python. O usuário digitará o comando e o manual aparecerá. Quando o usuário digitar a palavra 'FIM' ('END'), o programa será fechado. Importante: Use cores.
from time import sleep

#cores
cores_fundos = [
    "\033[m", # 0 - limpar
    "\033[42m", # 1 - verde
    "\033[7m", # 2 - branco
    "\033[46m", # 3 - ciano
    "\033[41m", # 4 - vermelho
    ]


def ajuda(palavra):
    texto(f"Acessando o manual do >{comando}<", cor=3)
    sleep(1)

    print(cores_fundos[2])
    help(palavra)
    print(cores_fundos[0])


def texto(mensagem, cor=0):
    tamanho = len(mensagem) + 4

    print(cores_fundos[cor],end="")

    print("~" * tamanho)
    print(f"{mensagem}")
    print("~" * tamanho)

    print(cores_fundos[0])


while True:
    texto("SISTEMA DE AJUDA PyHELP",cor=1)
    comando = str(input("Biblioteca ou função (fim = parar): ")).lower() .strip()

    if comando == "fim":
        texto("ATÉ LOGO!",cor=4)
        break

    ajuda(comando)
    

