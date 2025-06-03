#: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from ex111.utilidades import moeda

valor = float(input("Digite um valor: R$"))
desconto = int(input("Porcentagem de desconto: "))
aumento = int(input("Porcentagem de aumento: "))

moeda.resumo(valor, desconto, aumento)