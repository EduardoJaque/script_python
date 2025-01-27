import numpy as np
#crea array con 15 elementos aleatorios entre 1 y 100
random_array = np.random.randint(1, 100, size=(15))  
print("este es tu array de 15 elementos",random_array)

#mutitplica los numeros con un bucle for
multiplicacion = np.longdouble(1)
for i in range(len(random_array)):
    multiplicacion*=random_array[i]
print("multipliacion de elementos con bucle:  ",multiplicacion)
#multiplica con metodo numpy e imprime
result =np.prod(random_array, dtype=np.longdouble)
print("multipliacion de elementos con metodo: ",result)
if multiplicacion== result:
    print("los resultados son iguales")
else:   
    print("los resultados sin distintos")
# Crea otro array con 15 números decimales aleatorios entre 0 y 1
# genera un array con numeros desimales 
random_0_1 = np.random.rand(15)
#redondea los numeros desimales a dos desimas
random_0_1_redondeado = np.round(random_0_1, 2)
print("este es tu array de 15 elementos",random_0_1_redondeado)

#suma los dos array
#suma con bucle
suma1=0
print("la suma con bucle es ")
for i in range(len(random_array)):
    suma1+=random_array[i]+random_0_1_redondeado[i]
    print(round(suma1, 2),end=' ')
    suma1=0
print("")
#suma con metodo sum
result2 = np.add(random_array, random_0_1)
redondeado=np.round(result2, 2)
print("la suma con metodo es ")
print(redondeado)

#restar los 2 array
C=random_array- random_0_1_redondeado
print("la resta es")
print(C)
print("la resta con metdo es ")
resta = np.subtract(random_array,random_0_1_redondeado)
print(resta)

#multiplicacion de elemento por elemento 
multiplicacion=random_array*random_0_1_redondeado
print("multiplicacion con operador")
print(multiplicacion)
result_multi = np.multiply(random_array,random_0_1_redondeado)
print("resultado de multiplicacion con metodo")
print(result_multi)
#busca el nummero mayor
print("primer array",random_array)
print("segundo array",random_0_1_redondeado)
maximo=random_array.max()
maximo=np.round(maximo, 2)
print("Numero mayor array 1:",maximo)
maximo=random_0_1_redondeado.max()
maximo=np.round(maximo, 2)
print("Numero mayor array 2:",maximo)

#calcula la media


numero_medio=random_array.mean()
print("Numero medio arra 1",numero_medio)
numero_medio=random_0_1_redondeado.mean()
print("Numero medio arra 2",numero_medio)
#calcula la desviacion estandar 
std_dev = np.std(random_array)
std_dev=np.round(std_dev, 2)
print("Desviación estándar array 1:", std_dev)
std_dev = np.std(random_0_1_redondeado)
std_dev=np.round(std_dev, 2)
print("Desviación estándar array 2:", std_dev)
