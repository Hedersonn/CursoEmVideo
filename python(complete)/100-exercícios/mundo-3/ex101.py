# : Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# Função para ler a idade e mostrar o voto

def voto(nascimento):
    from datetime import date
    global idade

    ano_atual = date.today().year
    idade = ano_atual - nascimento

    if 65 >= idade >= 18:
        return f"Com {idade} anos: Voto obrigatório"
    if idade >= 65 or idade >= 16:
        return f"com {idade} anos: Voto Opicional"
    else:
        return f"Com {idade} anos: Voto Negado"
    
# Ler o ano de nascimento e mostrar a função    

ano_nascimento = int(input("Digite sua data de nascimento: "))
print(voto(ano_nascimento))
