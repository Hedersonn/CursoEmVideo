# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
import datetime

#Valores
ano_nascimento = int(input('Ano de nascimento: '))
ano_de_hoje = datetime.date.today().year
idade = ano_de_hoje - ano_nascimento
categoria = ''

#Condições

if idade < 0:
    print('ERRO')
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER'
print(f'Você é da categoria {categoria}')