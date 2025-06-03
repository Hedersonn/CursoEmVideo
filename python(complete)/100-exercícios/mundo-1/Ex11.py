#Largura e altura da parede.

largura = float(input('largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura *  largura

print(f'A altura da parede é de: {altura:.0f}m')#mostrar altura
print(f'A largura da parede é  de: {largura:.0f}m')#mostrar largura
print(f'A area é de: {area:.0f}m²')#mostrar área
print(f'Total de litros de tinta: {area / 2:.0f}l')#mostrar quantidade de tinta