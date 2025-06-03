#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da sua cidade: ')) .strip().upper()

print(f'A cidade começa com Santo? {'SANTO ' in cidade[:6]}')