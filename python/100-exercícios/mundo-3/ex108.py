# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from ex111.utilidades import moeda

valor = float(input("Digite o valor aqui: "))

print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"{moeda.moeda(valor)} com 15% de desconto é {moeda.moeda(moeda.diminuir(valor, 15))}")
print(f"{moeda.moeda(valor)} com 20% de desconto é {moeda.moeda(moeda.aumentar(valor, 20))}")
print(f"O dobro de {moeda.moeda(valor)} é de {moeda.moeda(moeda.dobro(valor))}")