
#pedir filas y columnas 
import random as rn
filas=int(input("cuantas filas quiere su matriz: "))
columnas=int(input("cuantas columnas quiere su matris "))
matriz=[]

#crear matris 
for i in range(filas):
    lista=[]
    for j in range(columnas):
        lista.append(rn.randint(1, 9))
    matriz.append(lista)

#identificar si es o no una matris

if len(matriz)==len(matriz[0]):
    valida_invalida=True
else:
    valida_invalida=False

if valida_invalida==True:
    
    #sumar filas
    for i, fila in enumerate(matriz):
        filas = sum(fila)
        print(f"la suma de la fila {i+1} es {filas}")
    
    # Sumar columnas
    suma_columnas = [0] * columnas
    for fila in matriz:
        for indice, valor in enumerate(fila):
            suma_columnas[indice] += valor

    # Imprimir la suma de cada columna
    for indice, suma in enumerate(suma_columnas):
        print(f"Suma de la columna {indice + 1}: {suma}")
else:
    print("L1 = [] y L2 = [] ")

