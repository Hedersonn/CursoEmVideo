#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Expressão >  "))
cont_parenteses = []

for parenteses in expressao:

    if parenteses == "(":
        cont_parenteses.append("(")
    elif parenteses == ")":
        if len(cont_parenteses) > 0:
            cont_parenteses.pop()
        else:
            cont_parenteses.append(")")
            break

if len(cont_parenteses) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão está incorreta!")