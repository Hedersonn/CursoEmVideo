#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Valores
primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
terceiro_numero = int(input('Terceiro número: '))

#Maior Número
if primeiro_numero > segundo_numero and terceiro_numero:
    maior = primeiro_numero
if segundo_numero > primeiro_numero and terceiro_numero:
    maior = segundo_numero
if terceiro_numero > primeiro_numero and segundo_numero:
    maior = terceiro_numero
print(f'O maior número é o {maior}')

#Menor número
if primeiro_numero < segundo_numero and terceiro_numero:
    menor = primeiro_numero
if segundo_numero < primeiro_numero and terceiro_numero:
    menor = segundo_numero
if terceiro_numero < primeiro_numero and segundo_numero:
    menor = terceiro_numero
print(f'O menor número é o {menor}')
