"""ADMINISTRACION DE PROYECTOS: 
Eres un gerente de proyectos y necesitas un programa para administrar 
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre, 
una descripción y un responsable asignado. Implementa un programa en 
Python que utilice un diccionario para almacenar la información de las 
tareas. El programa debe permitir agregar nuevas tareas, asignar 
responsables a las tareas existentes, actualizar las descripciones de las 
tareas y mostrar la lista completa de tareas y responsables. 
(Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de diccionarios) """

tareas_proyectos={"tarea 1":{"descripcion":"falta palo","responsable":"CB2 rojas"}
                  }
# El programa debe permitir agregar nuevas tareas
preguntar1=input("que quieres hacer:\nagregar nuevas tareas (1)\nasignar responsables a las tareas existentes (2)\nactualizar las descripciones de las tareas y mostrar la lista completa de tareas y responsables (3) \n\n").lower()
if preguntar1=="agregar" or preguntar1=="1":
    nombre_tarea=input("ingrese el nombre de la tarea: ")
    detalles_tarea=input("ingrese el detalle de la tarea: ")
    responsable_tarea=input("ingrese el responsable de la tarea: ")
    tareas_proyectos[nombre_tarea]={"descripcion":detalles_tarea,"responsable":responsable_tarea,}
# asignar responsables a las tareas existentes
elif preguntar1=="asignar" or preguntar1=="2":
    nombre_tarea=input("que tarea modificara: ")
    responsable_tarea=input("nuevo responsable: ")
    tareas_proyectos["tarea 1"]["responsable"] = responsable_tarea
# actualizar las descripciones de las tareas y mostrar la lista completa de tareas y responsables
elif preguntar1=="actualizar" or preguntar1=="3":
    print("solo debes modificar un parametro")
    nombre_tarea=input("ingrese el nombre de la tarea: ")
    detalles_tarea=input("ingrese el detalle de la tarea: ")
    responsable_tarea=input("ingrese el responsable de la tarea: ")

    if responsable_tarea=="":
        tareas_proyectos[nombre_tarea]["responsable"] = responsable_tarea
        tareas_proyectos[nombre_tarea]["descripcion"] = detalles_tarea
    elif detalles_tarea=="":
        tareas_proyectos[nombre_tarea]["responsable"] = responsable_tarea
        tareas_proyectos[nombre_tarea]["descripcion"] = detalles_tarea
    
else:
    print("error")
print(tareas_proyectos)









