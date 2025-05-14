#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

#Valores
segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento:'))
segmento3 = float(input('Terceiro segmento: '))
forma = ''

#Condições
if segmento1 + segmento2 > segmento3 and segmento2 + segmento3 > segmento1 and segmento1 + segmento3 > segmento2:
    print('Suas medidas formam um triângulo!')
    if segmento1 == segmento2 == segmento3:
        forma = 'EQUILÁTERO'
    elif segmento1 == segmento2 or segmento2 == segmento3 or segmento1 == segmento3:
        forma = 'ISÓSCELES'
    elif segmento1 != segmento2 and segmento2 != segmento3 and segmento1 != segmento3:
        forma = 'ESCALENO'
    print(f'Ele é um triângulo {forma}')
else:
    print('Suas medidas não formam um triângulo.')