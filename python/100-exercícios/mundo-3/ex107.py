#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from ex111.utilidades import moeda

v = float(input("Digite o valor em R$: "))

print(f"O dobro de R${v:.2f} e igual a R${moeda.dobro(v):.2f}")
print(f"Metade de R${v:.2f} e igual a R${moeda.metade(v):.2f}")
print(f"Com acrescimo de 5% o valor R${v:.2f} passou a valer R${moeda.aumentar(v, 5):.2f}")
print(f"Com desconto de 10% o valor de R${v:.2f} passou a valer R${moeda.diminuir(v, 10):.2f}")