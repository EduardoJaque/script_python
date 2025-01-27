import numpy as np
datos=np.array([
    ["2022-01-01","componnte 1","Lote A",80],
    ["2022-01-15","componnte 1","Lote B",90],
    ["2022-02-01","componnte 2","Lote C",85],
    ["2022-02-15","componnte 2","Lote D",91],
    ["2022-02-01","componnte 2","Lote E",75],
    ["2022-03-15","componnte 1","Lote F",90],
    ["2022-03-01","componnte 2","Lote G",80],
    ["2022-04-15","componnte 1","Lote H",70],
    ["2022-04-01","componnte 1","Lote I",75],
    ["2022-04-15","componnte 1","Lote J",60],
    ["2022-04-01","componnte 2","Lote K",95],
    ["2022-05-15","componnte 2","Lote L",85],
])

###CUAL ES EL COMPONENTE CON LA PUNTUACION DE CALIDAD MAS ALTA###
#BUSCAR EL INDICE MAS ALTO 
calificaciones=datos[:,3].astype(float)
componentes=datos[:,1]
fechas=datos[:,0]
lotes=datos[:,2]
indice = np.argmax(calificaciones)   
print(f'el componente con mejor puntuacion de calidad es "{componentes[indice]}" con fecha "{fechas[indice]}" y del lote "{lotes[indice]}" con una calificacion de "{calificaciones[indice]}" ')

###CUANTOS COMPONENTES SE PRODUJERON EN CADA MES###
#SEPARAR OR MES Y SUMAR POR MES
#de fechas usando split paso todo a numero
meses = np.array([int(fecha.split("-")[1]) for fecha in fechas]) 
valores_unicos, conteos = np.unique(meses, return_counts=True)

for i in valores_unicos:
    print(f'en el mes "{valores_unicos[i-1]}" se produjeron "{conteos[i-1]}" componentes')

###CUAL ES LA PUNTUACION DE CALIDAD PROMEDIO DE CADA COMPONENTE###

#crea una array 
suma_calificaciones = []
#separamos mos componentes en dos numeros 
componentes_numero = np.array([int(espacio.split(" ")[1]) for espacio in componentes]) 
#sacamos los valores unicos 
valores_unicos2, conteos2 = np.unique(componentes_numero, return_counts=True)

#con un bucle for iteramos en los mes 
for mes in componentes_numero:  
    #suma los elementos de la columna 
    suma = np.sum(calificaciones[componentes_numero == mes])
    #agrega la suma 
    suma_calificaciones.append(suma)
valores_suma, conteos_suma = np.unique(suma_calificaciones, return_counts=True)
promedios=np. round(valores_suma/conteos_suma,2)
print(f'la puntuacion de calidad promedio de cada componente es componente: {valores_unicos2[0]} promedio {promedios[0]}' )
print(f'la puntuacion de calidad promedio de cada componente es componente: {valores_unicos2[1]} promedio {promedios[1]}' )