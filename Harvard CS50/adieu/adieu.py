lista_nombres = []
while True:
    try:
        nombre = input("Name ")
        lista_nombres.append(nombre)
    except EOFError:
        break

if len(lista_nombres)==2:
    print(f"\nAdieu, adieu, to {lista_nombres[0]} and {lista_nombres[1]}.")
elif len(lista_nombres) > 1:
    ultimo_nombre = lista_nombres.pop()
    print(f"\nAdieu, adieu, to {', '.join(lista_nombres)}, and {ultimo_nombre}")
else:
    print(f"\nAdieu, adieu, to {lista_nombres[0]}")