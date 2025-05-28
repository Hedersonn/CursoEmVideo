#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade


def leiaInt(mensagem):

    while True:

        try:
            numero = int(input(mensagem))
        except:
            print("\033[33mERRO! Digite um número válido!\033[m")
            continue
        else:
            return numero
        

def leiaFloat(mensagem):

    while True:

        try:
            numero = float(input(mensagem))
        except:
            print("\033[33m ERRO! Digite um número válido!\033[m")
            continue
        else:
            return numero


numero_int = leiaInt("Digite um número inteiro:")
numero_real = leiaFloat("Digite um número real: ")

print(f"Número inteiro digitado> {numero_int}\nNúmero real digitado> {numero_real}")
