import moeda

v = float(input("Digite o valor em R$: "))

print(f"O dobro de {v:.2f} e igual a {moeda.dobro(v)}")
print(f"Metade de {v:.2f} e igual a {moeda.metade(v)}")
print(f"Com acrescimo de 10% o valor {v:.2f} passou a valer {moeda.aumentar(v)}")
print(f"Com desconto de 10% o valor de {v:.2f} passou a valer {moeda.diminuir(v)}")