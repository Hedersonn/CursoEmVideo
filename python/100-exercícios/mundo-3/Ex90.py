#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


# Descobrir sobre o aluno

aluno = {"Aluno": str(input("Nome do aluno: ")),
         "Média": float(input("Média do aluno: "))}
if aluno["Média"] >= 7.0:
    aluno["Condição"] = "APROVADO"
else:
    aluno["Condição"] = "REPROVADO"

# Pegar cada item do dict do aluno

for k, v in aluno.items():
    print(f"{k}: {v}")