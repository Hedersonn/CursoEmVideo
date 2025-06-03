
# Funções do ex109

def aumentar(preco=0, taxa=0, format=False):
    
    valor_tratado = preco + (preco * taxa / 100)

    if format:
        return moeda(valor_tratado)
    else:
        return valor_tratado


def diminuir(preco=0, taxa=0, format=False):
    valor_tratado = preco - (preco * taxa / 100)

    if format:
        return moeda(valor_tratado)
    else:
        return valor_tratado


def dobro(preco=0, format=False):
    valor_tratado = preco * 2

    if format:
        return moeda(valor_tratado)
    else:
        return valor_tratado


def metade(preco=0, format=False):
    valor_tratado = preco / 2

    if format:
        return moeda(valor_tratado)
    else:
        return valor_tratado
    

def moeda(preco=0,moeda="R$"):
    return f"{moeda}{str(preco).replace('.', ',')}"


def resumo(preco=0, desconto=0, aumento=0):

    print("-" * 35)
    print("Sistema Monetário".center(35))
    print("-" * 35)

    print(f"Preço analisado> \t{moeda(preco)}")
    print(f"Dobro do preço> \t{dobro(preco, True)}")
    print(f"Metade do preço> \t{metade(preco, True)}")
    print(f"{desconto}% de desconto> \t{diminuir(preco, desconto, True)}")
    print(f"{aumento}% de aumento> \t{aumentar(preco, aumento, True)}")
    print("-" * 35)