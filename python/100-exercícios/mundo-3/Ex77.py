# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Valores

vogais = "AEIOU"
palavras = ("Tupla",
            "Lista" ,
            "Operador" ,
            "Palavra" ,
            "Exercicio" ,
            "Python" ,
            "Programa" ,
            "Ovo" ,
            "Colher" ,
            "Linguiça"

)


# Loop

for palavra in palavras:
    print(f"{palavra} = ", end="")
    for vogal in vogais:
        if palavra.upper().count(vogal) > 0:
            print(vogal, end=" ")
    print()