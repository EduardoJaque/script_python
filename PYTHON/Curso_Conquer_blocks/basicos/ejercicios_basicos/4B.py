import numpy as np

datos=np.array([
    [20,70,1009,1],
    [17,35,1010,1],
    [22,35,1010,1],
    [30,60,1012,2],
    [20,50,1010,2],
    [22,40,1011,2],
    [24,45,1012,3],
    [25,65,1009,4],
    [28,40,1010,4],
    [30,40,1011,5],
    [30,35,1012,5],
    [15,40,1010,5],
    [18,50,1009,6],
    [20,55,1009,7],
    [22,60,1009,7],
    [24,65,1010,8],
    [25,65,1011,8],
    [26,70,1012,8],
    [27,65,1010,9],
    [28,60,1009,9],
    [22,55,1009,10],
    [23,50,1010,10],
    [15,45,1010,11],
    [16,40,1011,11],
    [17,43,1011,12],
    [18,40,1012,12],
    [19,55,1012,12],
])


#extraemos un array con los meses 
fechas = datos[:, 3]
#contamos las cantidades que se repiten (meses)
#valores unicos son los numeros sin repeticion (1-2-3-4-5-67-8-9-...)
#conteos es la cantidad de veces que se repiten los numeros unicos 
valores_unicos, conteos = np.unique(fechas, return_counts=True)


#temperatura 
#crea una array 
suma_temperatura = []
#con un bucle for iteramos en los 12 numeros de cada mes 
for mes in np.unique(fechas):
    #suma los elementos de la columna 0 cuando fechas es igual a mes creando una exprecion boleana
    suma = np.sum(datos[fechas == mes, 0])
    #agrega la suma a suma temperatura
    suma_temperatura.append(suma)
promedio_temperatura=np.round(suma_temperatura/conteos)


    
    


#humedad
suma_humedad = []

for mes in np.unique(fechas):
   
    suma = np.sum(datos[fechas == mes, 1])
 
    suma_humedad.append(suma)
promedio_humedad=np.round(suma_humedad/conteos)
#presion
suma_presion = []

for mes in np.unique(fechas):
   
    suma = np.sum(datos[fechas == mes, 2])
 
    suma_presion.append(suma)
promedio_presion=np.round(suma_presion/conteos)

for indice, mes in enumerate(valores_unicos):
    print(f"El mes {mes}  [temperatura {promedio_temperatura[indice]}] -- humedad[{promedio_humedad[indice]}] --[presion{promedio_presion[indice]}]")