#  Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Função

def escreva(texto):
    tamanho = len(texto) + 4
    print("=" * tamanho)
    print(f"  {texto}")
    print("=" * tamanho)

# Mostar função

escreva(str(input("Digite uma Frase: ")).title().strip())