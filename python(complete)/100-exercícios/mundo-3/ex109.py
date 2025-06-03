# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from ex111.utilidades import moeda

valor = float(input("Digite o valor aqui: "))
    
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}")
print(f"{moeda.moeda(valor)} com 15% de desconto é {moeda.diminuir(valor, 15, format=True)}")
print(f"{moeda.moeda(valor)} com 20% de acréscimo é {moeda.aumentar(valor, 20, format=True)}")
print(f"O dobro de {moeda.moeda(valor)} é de {moeda.dobro(valor, format=True)}")