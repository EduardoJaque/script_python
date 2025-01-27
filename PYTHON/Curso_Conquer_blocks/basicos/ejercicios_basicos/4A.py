import numpy as np

datos=np.array([
    ["2022-01-01",200,"ropa"],
    ["2022-01-03",300,"alimentos"],
    ["2022-01-04",100,"electronicos"],
    ["2022-01-05",400,"ropa"],
    ["2022-02-01",100,"ropa"],
    ["2022-02-02",100,"alimentos"],
    ["2022-02-04",100,"ropa"],
    ["2022-03-02",100,"electronicos"],
    ["2022-03-02",700,"alimentos"],
    ["2022-03-03",100,"ropa"],
    ["2022-03-05",100,"electronicos"],
    ["2022-03-05",100,"ropa"],
    ["2022-04-02",100,"alimentos"],
    ["2022-04-03",50,"ropa"],
    ["2022-04-05",100,"ropa"],
    ["2022-04-05",100,"ropa"],
    ["2022-04-05",10,"ropa"],
    ["2022-04-05",100,"alimentos"],
    ["2022-04-06",200,"ropa"],
    ["2022-04-06",100,"electronicos"],
    ["2022-04-07",300,"alimentos"],
    ["2022-04-08",100,"electronicos"],
])
#saco los precios de los alimentos
numeros = datos[:, 1].astype(int)
#saco las fechas 
fechas = datos[:, 0]
#de fechas usando split paso todo a numero
meses = np.array([int(fecha.split("-")[1]) for fecha in fechas])
#concateno las fechas y los precios en la variable concatenado
concatenado = np.column_stack((numeros, meses))
# aparto los meses
categorias = np.unique(concatenado[:, 1])
print(categorias)
# Sumar los valores por meses 
suma_por_categoria = np.array([np.sum(concatenado[concatenado[:, 1] == categoria, 0]) for categoria in categorias])

# Crear un array bidimensional con las categorías y sus sumas
resultado = np.column_stack((categorias, suma_por_categoria))

print("Suma de valores por categoría:\n", resultado)


