import numpy as np
# Solicitar al usuario que indique una longitud para el array
valor = int(input("Indique una longitud: "))
array_1 = np.ones((valor))
print("array 1:",array_1)
#cambiar estructura del array
array_1=np.reshape(array_1,(2,4))
matriz_identidad=np.reshape(array_1,(2,4))
print("matriz de identidad: ",matriz_identidad)
result1 = np.concatenate((array_1,matriz_identidad), axis=0)
result2 = np.concatenate((array_1,matriz_identidad), axis=1)
print("arrays concatenados\nfilas ",result1,"\ncolumnas",result2)