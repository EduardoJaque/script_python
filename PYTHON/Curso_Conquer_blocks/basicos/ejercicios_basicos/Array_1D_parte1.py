#importo numpy
import numpy as np
#creo array 8 elemtos que contenen  0 y los imprimo
array_1=np.zeros((8))
print ("array oroginal con 0",array_1)
#le suo 2 atodo los array_1
array_con_2=array_1[:]+2
print("array con 2 ",array_con_2)
#creo un segundo array con los numeros pares del 1 al 10 y los imprimo
array_2=np.arange(2,11,2)
print("array original ",array_2)
#creo una variable para sumar los numeros pares en un bucle for  y los imprimo
suma=0
for i in range(len(array_2)):
    suma= suma+array_2[i]
print("suma usando un bucle ",suma)
#con el metodo sum sumo los elemntos del array 2 y los imprimo
print("suma usando un metodo ",array_2.sum())
if array_2.sum()== suma:
    print("son iguales")
else:
    print("son diferentes")
#creo un array revertido del array 2
array_2_rvertido=[]
array_2_rvertido[:]=array_2[::-1]
print("array revertido: ", array_2_rvertido)

# con los array 2 y revertido busco los elementos iguales y los imprimo
intersection = np.intersect1d(array_con_2,array_2_rvertido)
print("los numeros comunes entre array revertido y array dos son: ",intersection)
intersection2=np.intersect1d(array_2,array_2_rvertido)
print("los numeros comunes entre array revertido y array con 2 son: ",intersection)
# Solicitar al usuario que indique una longitud para el array
valor = int(input("Indique una longitud: "))
array_3 = np.ones((valor))
print(array_3)
