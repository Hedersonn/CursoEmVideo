#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

#Valores
numero = randint(1, 10)
escolha = int(input('Digite um número de 1 a 10: '))
tentativas = 1

#Loop
while not escolha == numero:
    tentativas += 1
    escolha = int(input('Errado, HAHA! Digite novamente: '))

print(f'''Você acertou! Eu escolhi o {numero}
Total de tentativas: {tentativas}''')