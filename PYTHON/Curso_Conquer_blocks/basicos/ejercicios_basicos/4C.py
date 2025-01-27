#array con datos de peliculas 
import numpy as np
peliculas=np.array ([
    ["pelicula 1","comedia",120,1990,9.9],
    ["pelicula 2","accion",110,2005,8.9],
    ["pelicula 3","drama",95,2010,8.4],
    ["pelicula 4","accion",100,1985,8.9],
    ["pelicula 5","comedia",130,2015,7.7],
    ["pelicula 6","drama",115,2000,8.7],
    ["pelicula 7","accion",90,1995,8.1],
    ["pelicula 8","comedia",105,2010,8.8],
    ["pelicula 9","accion",125,1980,7.5],
    ["pelicula 10","drama",120,2000,7.8],
    ["pelicula 11","comedia",95,1999,8.1],
    ["pelicula 12","drama",130,1993,6.7],
    ["pelicula 13","accion",110,1994,8.2],
    ["pelicula 14","comedia",122,1995,7.4],
    ["pelicula 15","accion",125,1996,6.8],
    ["pelicula 16","accion",129,1997,8.0],
])
genero=peliculas[:,1]
años=peliculas[:,3].astype(int)

numeros=peliculas[:,2:].astype(float)
# busco la cantidad de repeticiones de los generos de la pelicula
valores_unicos, conteos = np.unique(genero, return_counts=True)

# genero de pelicula mas popular 
# calcular el promedio por genero imprimer el mas alto 
suma_genero= []
# con un bucle for iteramos para sumar los elementos de indice 0 (calificacion)
for i in np.unique(genero):
    suma= np.sum(numeros[genero == i, 2])
    #suma los elementos de la columna 0 cuando fechas es igual a mes creando una exprecion boleana
    suma_genero.append(suma)
# Calcular los promedios
promedios = [np.round(suma_genero[i] / conteos[i], 2) for i in range(len(valores_unicos))]

# Encontrar el índice del promedio más alto el cual se asemeja a los valores unicos
indice_max = np.argmax(promedios)
# imprime el genero  y promedio mayor
print(f'el genero mas popular es "--{valores_unicos[indice_max]}--" con una calificacion promedio de  "..{promedios[indice_max]}.." ')

# cuantas peliculas se lansaron en cada decada 
# Calcular la década correspondiente a cada año (dejar los años justos)
decadas = (años // 10) *10
# separo en decadas 
decadas_solas=np.unique(decadas)

# Contar las películas en cada década usando np.count_nonzero
conteo_decadas = {decada: np.count_nonzero(decadas == decada) for decada in decadas_solas}
print(conteo_decadas)  




#duracion promedio de cada pelicula 
#calcular duracion promedio por genero 
suma_tiempo=[]
for i in np.unique(genero):
    suma= np.sum(numeros[genero==i, 0])
    #suma los elementos de la columna 0 cuando fechas es igual a mes creando una exprecion boleana
    suma_tiempo.append(suma)
promedios2 = [np.round(suma_tiempo[i] / conteos[i], 0) for i in range(len(valores_unicos))]

# Encontrar el índice del promedio más alto el cual se asemeja a los valores unicos
indice_max2 = np.argmax(promedios2)
# imprime el genero  y promedio mayor
print(f'el genero con mayor tiempo promedio es "--{valores_unicos[indice_max2]}--" con un promedio de "..{promedios2[indice_max2]}.." ')

