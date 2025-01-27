"""REGISTRO DE ASISTENCIAS: 
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus 
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y 
una lista de fechas en las que asistió a clases. Implementa un programa 
en Python que utilice un diccionario para almacenar la información de las 
asistencias. El programa debe permitir registrar la asistencia de los 
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de 
estudiantes y las fechas en las que asistieron.
 (Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de listas)"""
#El programa debe permitir registrar la asistencia de los estudiantes
diccionario_asistencia={}
lista=[]
lista2=[]
boleano1=True
boleano=True
print('si desea salir, precione "|N| |n| |0|" de lo contrario presione "|S| |s| |1|"')
#AGRREGAR ESTUDIANTES Y SUS ASIGNATURAS
while boleano1:
    estudiante1=input("que estudiante es: ")
    while boleano:
        asgnatura=input("indique la fecha: ").lower()
        lista.append(asgnatura)
        if asgnatura== "no" or asgnatura=="n" or asgnatura==0:
            boleano=False
    lista.pop()
    copia=lista[:]
    diccionario_asistencia [estudiante1]= copia
    lista.clear()
    otra_pregunta=input("desea agregar otro estudiante: ").lower()   

    if otra_pregunta== "si" or otra_pregunta== "s" or otra_pregunta== 1:
            boleano1=True
            boleano=True
    elif otra_pregunta== "no" or otra_pregunta=="n" or otra_pregunta== 0:
            boleano1=False
     
continuar2= True
#agregar nuevas fechas de asistencia
preguntar=input("desea agregar nuevas asisitencias: ")

if preguntar=="s"or preguntar=="si" or preguntar==1:
    estudiante2=input("ha que estudiante quiere agregar asistenca: ")
    while True:
        asignatura=input("indique la fecha: ")
        lista2.append(asignatura)
        if asignatura== "no" or asignatura=="n" or asignatura== 0:
            break
    diccionario_asistencia[estudiante2]=lista2

#mostrar la lista de estudiantes y las fechas en las que asistieron
print(diccionario_asistencia)

