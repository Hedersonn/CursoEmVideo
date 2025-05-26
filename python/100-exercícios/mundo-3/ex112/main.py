# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
from ex111.utilidades111 import moeda

# Função do ex112

def leiaDinheiro(valor):
    valor = str(valor).strip()
    if valor.isnumeric():
        return moeda.resumo(valor, 10, 5)
    else:
        return "Erro! Digite um valor válido!"

leiaDinheiro(input("Digite um número: "))