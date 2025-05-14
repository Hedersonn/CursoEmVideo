#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#Valores
termo = int(input('Primeiro termo: '))
razao = int(input('Digite a razao: '))


#Contadores
contador = 0
valor_termos = termo

#Loops
while contador < 10:
    print (f'{"(" if contador == 0 else ""}{valor_termos}{"," if contador < 9 else ")"}', end='')
    quantidade_termos += 1
    valor_termos += razao
