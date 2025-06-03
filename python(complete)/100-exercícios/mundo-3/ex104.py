# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


# Função para ler um número inteiro

def leiaInt(mensagem):
    n = input(mensagem)
    while not n.isnumeric():
        print("\033[31m Erro! Digite um número inteiro válido!\033[m")
        n = input(mensagem)
    return int(n)