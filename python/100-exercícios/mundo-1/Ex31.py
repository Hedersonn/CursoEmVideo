#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


#Valores
distancia = float(input('Qual a distância em KM: '))

#Condições
if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45
print(f'O valor deu R${valor:.2f} pela distância de {distancia:.2f}KM.')
