# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

#Valores
velocidade = float(input('Qual a sua velocidade? '))
print(f'A sua velocidade foi de {velocidade:.2f}km/h.')

print('+=' * 20)

#Condições
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f'Você foi multado em R${multa:.2f} por exceder {velocidade - 80:.2f}km/h')
else:
    print('Você está na velocidade.')
print('+=' * 20)