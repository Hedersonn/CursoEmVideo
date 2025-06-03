#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)



def notas(*notas, sit=False):
    """
    *notas: Recebe várias notas
    sit: True >mostra a situação da média da turma< | False >Não mostra<
    return > Guardar e retornar o dicionário (resumo)
    """
    media = menor = maior = 0

    resumo = {
        "quantidade": len(notas),
        "maior": max(notas),
        "menor": min(notas),
        "media": sum(notas) / len(notas)
    }

    if sit:
        media = resumo["media"]
        if media < 6:
            resumo["situacao"] = "Ruim"
        elif media < 7:
            resumo["situacao"] = "Razoável"
        else:
            resumo["situacao"] = "Boa"

    return resumo

print(notas(2,5,3, sit=True))
help(notas)

        
