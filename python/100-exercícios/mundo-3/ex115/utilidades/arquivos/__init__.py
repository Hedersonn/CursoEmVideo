# Verificar se um arquivo está ou não criado

def verificador_arquivo(arq):

    try:
        with open(f"C:/Users/pajeh/OneDrive/Documentos/estudos/CursoEmVideo/python/100-exercícios/mundo-3/ex115/{arq}", "r") as arquivo:
            arquivo = arquivo.read()
    except:
        return False
    else:
        return True
    

# Criar um arquivo

def criar_arquivo(arq):
    from utilidades.grafica import cor 

    try:
        with open(f"C:/Users/pajeh/OneDrive/Documentos/estudos/CursoEmVideo/python/100-exercícios/mundo-3/ex115/{arq}", "wt+") as arquivo:
            arquivo = arquivo.read()

    except:
        print(cor(9, "Houve um problema!"))
    else:
        print(f"Arquivo {arquivo} criado com sucesso!")


# Ler um arquivo

def ler_arquivo(arq):
    from utilidades.grafica import cor

    with open(f"C:/Users/pajeh/OneDrive/Documentos/estudos/CursoEmVideo/python/100-exercícios/mundo-3/ex115/{arq}", "r") as arquivo:
        try:
            for linha in arquivo:
                dado = linha.split(";")
                dado[1] = dado[1].replace("\n", "")
                print(f"{dado[0]:<40}{dado[1]:>3} anos")
        except:
            print(cor(9, "Tivemos um problema. Tente verificar o arquivo."))


# Adicionar itens em um arquivo

def adicionar_arquivo(arq, usuario="desconhecido", idade=0):
    with open(f"C:/Users/pajeh/OneDrive/Documentos/estudos/CursoEmVideo/python/100-exercícios/mundo-3/ex115/{arq}", "a") as arquivo:
            arquivo.write(f"{usuario};{idade}\n")


# Verificar um número inteiro

def leiaInt(mensagem):

    while True:

        try:
            numero = int(input(mensagem))
        except:
            print("\033[33mERRO! Digite um número válido!\033[m")
            continue
        else:
            return numero
        