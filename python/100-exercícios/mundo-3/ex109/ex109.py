# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from .ex111 import moeda

valor = float(input("Digite o valor aqui: "))
    
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}")
print(f"{moeda.moeda(valor)} com 15% de desconto é {moeda.diminuir(valor, 15, format=True)}")
print(f"{moeda.moeda(valor)} com 20% de acréscimo é {moeda.aumentar(valor, 20, format=True)}")
print(f"O dobro de {moeda.moeda(valor)} é de {moeda.dobro(valor, format=True)}")