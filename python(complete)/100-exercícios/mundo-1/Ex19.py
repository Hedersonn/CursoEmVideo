#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

from random import choice

aluno1 = str(input('Primeiro Aluno(a): '))
aluno2 = str(input('Segundo Aluno(a): '))
aluno3 = str(input('Terceiro Aluno(a): '))
aluno4 = str(input('Quarto Aluno(a): '))

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno(a) sorteado foi {choice(alunos)}.')