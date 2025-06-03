# Função do ex112

def leiaDinheiro(texto):
    
    from ex111.utilidades.moeda import resumo
    
    while True:
        valor = input(texto).replace(",", ".").strip()

        if valor.isalpha() or valor.isspace() or valor == "":
            print("Erro! Digite um valor válido!")
        else:
            valor = float(valor)
            return resumo(valor, 10, 10)