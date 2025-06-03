#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

#Valores
peso = float(input('Seu peso: '))
altura = float(input('Sua altura:'))
imc = peso / (altura ** 2)

#Condições
print(f'Seu IMC: {imc:.1f}')
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc < 25:
    print(f'PESO IDEAL!')
elif imc < 30:
    print('SOBREPESO!!')
elif imc < 40:
    print('OBESIDADE!!')
else:
    print('OBESIDADE MÓRBIDA')