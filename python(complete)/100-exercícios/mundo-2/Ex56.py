#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


#Contadores
quant_pessoas = 0
idade_total = 0
nome_homem = ''
idade_homem = 0
quant_mulheres = 0

#Loops
for i in range(1, 5):
    quant_pessoas += 1

    print(f'{i}ª Pessoa:')
    print('-' * 20)
    nome = str(input('Nome: ')) .title() .strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')) .upper() .strip()
    print('-' * 20)

    idade_total += idade
    if sexo == 'M' and idade > idade_homem:
        idade_homem = idade
        nome_homem = nome
    else:
        if sexo == 'F' and idade < 20:
            quant_mulheres += 1

media = idade_total / quant_pessoas
print(f'''A média do grupo é de {media} anos.
O homem mais velho é o {nome_homem}, com {idade_homem} anos.
Têm {quant_mulheres} mulheres com menos de 20 anos.''')
