# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# Função para ler o fatorial de um número

def fatorial(numero, show= False):
    """Calcule a fatorial de um número:

    parâmetro >numero< = numero para o fatorial;
    parâmetro >show< = Decide se quer mostrar ou não a conta(opcional);
    return >n< = retorna o número tratado.
    """

    total = 1
    for n in range(numero, 0, -1):
        total *= n
        if show:
            print(n, end=" x " if n > 1 else " = ")
    return total

# Programa Principal

print(fatorial(5, True))
help(fatorial)