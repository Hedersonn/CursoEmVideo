
        #maneira otimizada, treinada e estudada.
#importações
from time import sleep
from random import randint

#cores
azul_negrito = '\033[34:1m'
inversao = '\033[7m'
negrito = '\033[1m'
limpa = '\033[m'
azul_claro = '\033[36m'
vermelho = '\033[31m'
sublinhado = '\033[4m'

#escolha do computador
jokenpo = ('Pedra', 'Papel', 'Tesoura')
jokenpo_numero = randint(0, 2)

#escolha do humano
escolha = int(input(negrito + f'''Faça a Sua Escolha:{limpa}
    [ 1 ] {sublinhado + negrito}Pedra{limpa}
    [ 2 ] {sublinhado + negrito}Papel{limpa}
    [ 3 ] {sublinhado + negrito}Tesoura{limpa}
> '''))
escolha -= 1

if escolha not in [0, 1, 2]:
    print(vermelho + negrito + sublinhado + 'Erro!' + limpa)
    quit()

#palavra jokenpo
sleep(0.4)
print(f'{sublinhado + negrito}JO', end='')
sleep(0.5)
print(f'KEN', end='')
sleep(0.5)
print(f'PO{limpa}')

#mostrar quem venceu
print( azul_negrito + '+-' * 12 + limpa )
print(f'''{azul_claro + sublinhado + negrito}Eu escolhi {jokenpo[jokenpo_numero]}
Você escolheu {jokenpo[escolha] + limpa}''')
print(azul_negrito + '+-' * 12 + limpa)

#condições do jogo
if jokenpo_numero == escolha:
    print(negrito +'Empate!' + limpa)
elif escolha == 0 and jokenpo_numero == 1\
        or escolha == 1 and jokenpo_numero == 2\
        or escolha == 2 and jokenpo_numero == 0:
    print(azul_claro + negrito + 'Ganhei! HAHA!!' + limpa)
else:
    print(vermelho + negrito + 'Perdi!' + limpa)
    