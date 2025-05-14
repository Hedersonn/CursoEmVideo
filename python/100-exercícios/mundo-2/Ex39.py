#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
from time import sleep

#Valores
ano_nascimento = int(input('Qual o ano de seu nascimento? '))



#Conversão
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento

print('Calculando...')
sleep(2)
print(f'Estamos no ano de {ano_atual}')

#Condições
if idade < 18:
    falta = 18 - idade
    print(f'Você está com {idade} anos, falta {falta} ano(s) para se alistar!')
elif idade > 18:
    passou = idade - 18
    print(f'Você está com {idade} anos, passaram {passou} anos(s) para se alistar!')
else:
    print('Você está na idade de se alistar!')