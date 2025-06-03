#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep
alunos = []
# Cadastro de alunos

while True:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("1ª Nota > "))
    nota2 = float(input("2ª Nota > "))
    alunos.append([nome, nota1, nota2])
    
    continuar = str(input("Quer continuar? S|N > ")).lower().strip()[0]
    if continuar == 'n':
        print("Fechando programa..")
        sleep(1.2)
        break

# Exibe boletim geral

print("\n", "-_" * 25, "\n")
print(f"{'Nº':<5}{'NOME':<20}{'MÉDIA':>10}")
print("-" * 40)
for i, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f"{i + 1:<5}{aluno[0]:<20}{media:>10.1f}")
print("-" * 40)

# Consulta individual

while True:
    escolha = int(input("\nDigite o número do aluno <999 CANCELA> ")) - 1
    if escolha == 998:
        print("Saindo do sistema de boletins...")
        break
    if 0 <= escolha < len(alunos):
        print(f"\nNotas de {alunos[escolha][0]}:")
        print(f" 1ª Nota: {alunos[escolha][1]}")
        print(f" 2ª Nota: {alunos[escolha][2]}")
    else:
        print("Número inválido. Tenta de novo.")
