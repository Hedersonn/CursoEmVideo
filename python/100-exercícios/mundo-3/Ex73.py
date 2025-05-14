# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Sao Paulo.


# Valores

times = (
    "Palmeiras", "Red Bull Bragantino", "Flamengo", "Cruzeiro", "Fluminense",
    "Bahia", "Ceará", "Corinthians", "Internacional","Atlético Mineiro",
    "São Paulo", "Botafogo", "Grêmio", "Vasco da Gama", "Juventude", 
    "Mirassol", "Fortaleza", "Vitória", "Santos", "Recife"
)

# Primeiros 5 times

print(" Top 5 ". center(25, "="))
print("")

for colocacao, time in enumerate(times[ : 5]):
    print(f"{colocacao + 1}º {time}")

# Ultimos 4 colocados

print("")
print(" 4 Ultimos ".center(25, "="))
print("")

for colocacao, time in enumerate(times[-4:]):
    print(f"{colocacao + 17}º {time}")

# Times em ordem alfabetica

print("")
print(" Ordem alfabetica ".center(25, "="))
print("")

for time in sorted(times):
    print(time)

# Colocacao do time de Sao Paulo

print("")
print("São Paulo".center(25, "="))
print("")

print(f"São Paulo esta em {times.index("São Paulo") + 1}º")

print("")
print("-" * 25)





