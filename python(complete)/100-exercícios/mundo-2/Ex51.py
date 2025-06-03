#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

#Valores
primeiro_termo = int(input('Termo: '))
razao = int(input('Razão: '))
termos = primeiro_termo + (11 - 1) * razao

#Repetição
for i in range(primeiro_termo, termos, razao):
    print(i, end=' - ')
print('Fim!')