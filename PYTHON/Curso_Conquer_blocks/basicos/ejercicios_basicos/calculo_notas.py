import numpy as np
#ingresar el nombre del estudiante, asociarlo a un numero (fila)
nombre_estudiantes=["jake","alvarez","boza"]
notas=[[7,7,7,7,],[4,5,7,1],[4,4,4,4]]
#calcular promedio de notas segun porcentaje (examen 30%*2, trabajo final 30%, participacion enclases 10%
#crea matriz con porcentajes
porcentaje=[30,30,30,10]
#multiplica las notas por porcentajes 
result_multi = np.multiply(notas,porcentaje)
#suma las filas y divide por el porcentaje final
promedio= np.sum(result_multi, axis=1)/100

#segun fila=alumno imprimir notas y promedio final 
print("las notas de los alumnos son las siguientes: ")
for i in range(len(nombre_estudiantes)):
    print("estudiante",nombre_estudiantes[i],"notas",notas[i],"promedio",promedio[i])

