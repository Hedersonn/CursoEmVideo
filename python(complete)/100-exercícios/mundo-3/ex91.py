#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.


from datetime import date

ano_atual = date.today().year

nome = str(input("Digite seu nome: "))
nascimento = int(input("Sua data de nascimento: "))
idade = ano_atual - nascimento
cpts =  int(input("CPTS |[0] NÃO POSSUI > "))

pessoa = {
    "Nome": nome,
    "Idade": idade,
    "CTPS": cpts 
}

if pessoa["CTPS"] > 0:
    pessoa["Contratação"] = int(input("Ano de contratação: "))
    pessoa["Salário"] = float(input("Salário: "))
    pessoa["Aposentadoria"] = (pessoa["Contratação"] + 15) - nascimento

for k, v in pessoa.items():
    print(f"{k}: {v}")