#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

#Valores
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

#Loop
while True:
    print('=' * 40)
    escolha = int(input('''Digite:
    
    [ 1 ] Soma
    [ 2 ] Multiplição
    [ 3 ] Maior número
    [ 4 ] Digitar novamente
    [ 5 ] Sair
    > '''))
    print('=' * 40)
    if escolha == 1:
        soma = numero1 + numero2
        print(f'{numero1} + {numero2} = {soma}')
    elif escolha == 2:
        multiplica = numero1 * numero2
        print(f'{numero1} x {numero2} = {multiplica}')
    elif escolha == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é maior que o {numero2}.')
        elif numero1 < numero2:
            print(f'O número {numero2} é maior que o {numero1}.')
        else:
            print('Os dois números são iguais.')
    elif escolha == 4:
        numero1 = int(input('Primeiro número: '))
        numero2 = int(input('Segundo número: '))
    elif escolha == 5:
        print('Saindo..')
        break
    else:
        print('Opção inválida!')
