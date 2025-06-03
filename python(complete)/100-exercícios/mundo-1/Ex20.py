#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = str(input('Primeiro Aluno(a): '))
aluno2 = str(input('Segundo Aluno(a): '))
aluno3 = str(input('Terceiro Aluno(a): '))
aluno4 = str(input('Quarto Aluno(a): '))

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print(f'A ordem da apresentação será:\n{alunos}')