# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.


# Função do ex112

def leiaDinheiro(valor=0):
    valor = str(valor)
    if valor.isalpha() or valor.isalnum() or valor.isspace() or valor.isacii():
        print("Erro, digite um ")

leiaDinheiro()