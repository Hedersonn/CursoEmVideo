#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#Escolha
numero = int(input('Digite um número: '))

#Repetição
for tabuada in range(1, 11):
    multiplicacao = numero * tabuada
    print(f'{numero} x {tabuada} = {multiplicacao}')