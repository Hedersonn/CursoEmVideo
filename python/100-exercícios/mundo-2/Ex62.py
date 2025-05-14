#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print("=" * 40)
print("PROGRESSÃO ARITMÉTICA".center(40))
print("=" * 40)

# Valores
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
total_termos = 0
mais = 10  # Começa mostrando 10 termos

# Loop
while mais != 0:
    contador = 0
    while contador < mais:
        print(f"{termo}", end=" → " if contador < mais - 1 else " → FIM\n")
        termo += razao
        contador += 1
        total_termos += 1
    print(f"\nTotal de termos mostrados: {total_termos}")
    mais = int(input("Quantos termos a mais você quer mostrar? (0 para sair): "))

print("=" * 40)
print(f"PA finalizada com {total_termos} termos exibidos.")
print("=" * 40)
