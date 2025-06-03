# Vamos criar um menu em Python, usando modularização com opcao de ver pessoa cadastrada, cadastrar nova pessoa e sair do sistema.
#Criar um arquivo e colocar as pessoas com seu nome e idade.

from utilidades.arquivos import *
from utilidades.grafica import *

verificar_arquivo = "usuarios.txt"
if not verificador_arquivo(verificar_arquivo):
    criar_arquivo(verificar_arquivo)

while True:

    escolha = menu("Pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema")

    if escolha == 1:
        linhas(texto="Pessoas Cadastradas")
        ler_arquivo("usuarios.txt")
    elif escolha == 2:
        linhas(texto="Adicionar Cadastro")
        nome = str(input("Digite o nome: "))
        idade = leiaInt("Digite a idade: ")
        adicionar_arquivo("usuarios.txt", nome, idade)
        print("Cadastro feito com sucesso!")
    elif escolha == 3:
        linhas(texto="Fechando o programa")
        break
