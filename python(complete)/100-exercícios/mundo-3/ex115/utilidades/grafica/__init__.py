# Mostrar uma linha c/s texto

def linhas(formato="-", tamanho=50, texto=False):

    if not texto:
        print(formato * tamanho)

    else:
        print(formato * tamanho)
        print(f"{texto}".center(tamanho))
        print(formato * tamanho)


# Menu de cores

cores = [
    "\033[m", # 0 limpa
    "\033[30m", # 1 preto
    "\033[31m", # 2 vermelho
    "\033[32m", # 3 verde
    "\033[33m", # 4 amarelo
    "\033[34m", # 5 azul
    "\033[35m", # 6 magenta
    "\033[36m", # 7 ciano
    "\033[37m", # 8 cinzac
    "\033[90m", # 9 cincae
    "\033[91m", # 10 vermelhoc
    "\033[92m", # 11 verdec
    "\033[93m", # 12 amareloc
    "\033[94m", # 13 azulc
    "\033[95m", # 14 magentac
    "\033[96m", # 15 cianoc
    "\033[97m", # 16 branco
    "\033[1m", # 17 negrito
    "\033[7m" # 18 inverte
    ]

def cor(cor=0, texto=False):

    if texto:
        frase_com_cor = f"{cores[cor]}{texto}{cores[0]}"
        return frase_com_cor
    else:
        print(cores[cor], end="")

    
# Montar um menu

def menu(*texto):
    quantidade = len(texto)

    linhas(texto="Menu Principal")
    for numeracao, txt in enumerate(texto):
        print(f"{cor(9, numeracao + 1)} - {cor(6, txt)}")
    linhas()

    while True:

        try:
            cor(13)
            escolha = int(input("Sua opção > "))
            cor()

            if 1 <= escolha <= quantidade:
                return escolha
            else:
                print(cor(10, "Opção inválida!"))
        except:
            print(cor(10, "Erro! Digite um valor válido!"))