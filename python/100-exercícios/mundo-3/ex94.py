# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média


# Valores

pessoas = []
mulheres = []
idades = 0

# Loop

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Digite o nome: ')) .capitalize() .strip()

    while True:
        pessoa['sexo'] = str(input('Digite o sexo F|M : ')).upper() .strip() [0]
        if pessoa['sexo'] in "FM":
            break
        else:
            print('Erro! Digite apenas F ou M.')
 
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Digite a idade: '))
    
    idades += pessoa['idade']
    pessoas.append(pessoa.copy())
    
    while True:
        continuar = str(input('Quer adicionar mais usuarios? S|N : ')).upper() .strip() [0]
        if continuar in "SN":
            break
        else:
            print("Erro! Digite apenas S ou N.")
    if continuar == 'N':
        print('Fechando programa.')
        break

# Valores finais

media = idades / len(pessoas)

print("-=" * 20)

print(f"Ao todo, foram {len(pessoas)} pessoa{'s' if len(pessoas) > 1 else ''} cadastradas.")
print(f"A média das idades é de {media:.0f}")
print("Mulheres cadastradas:", ', '.join(mulheres) if mulheres else "Nenhuma mulher cadastrada.")

acima = [p for p in pessoas if p['idade'] > media]
print(f"Pessoas acima da idade média:")
for p in acima:
    print(f"{p['nome']} ({p['idade']} anos)")