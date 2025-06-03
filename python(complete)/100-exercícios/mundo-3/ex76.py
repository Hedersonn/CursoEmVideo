#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Valores

produtos = ("Lápis", 3.50, 
            "Borracha", 2.30, 
            "Caderno", 17.59, 
            "Notebook", 1599.99,
            "Cabo HDMI", 37.99,
            "Relógio De Parede", 50.00
)


print(f"{'LISTAGEM DE PREÇOS':^40}")
print("=" * 45)

# Repetição

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f"{nome:<30} R$ {preco:>7.2f}")

print("=" * 45)
