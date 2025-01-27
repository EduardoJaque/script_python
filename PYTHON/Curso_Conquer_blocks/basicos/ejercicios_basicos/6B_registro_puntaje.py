"""REGISTRO DE PUNTAJES: 
Implementa un programa en Python que permita registrar y mantener un 
seguimiento de los puntajes de un juego. El programa debe permitir a los 
jugadores ingresar sus nombres y puntajes, almacenarlos en un 
diccionario y proporcionar funcionalidades para mostrar el puntaje más 
alto, el promedio de puntajes y la cantidad total de jugadores"""
diccionario_puntajes={}
boleano=True
#ingresar sus nombres y puntajes
while boleano:
    nombre=input("ingrese nombre de los jugadores: ")
    puntaje=input("ingrese su puntaje: ")
    #almacenarlos en un diccionario
    diccionario_puntajes[nombre]=puntaje
    if puntaje=="n":
        diccionario_puntajes.pop(nombre)
        boleano = False
#proporcionar funcionalidades para mostrar el puntaje más alto
maximo=max(diccionario_puntajes.values())
print("el puntaje maximo es:",maximo)
#el promedio de puntajes
total=0
Contador=0
mayor=0
for nombre, clave in diccionario_puntajes.items():
    numero=int(clave)
    if numero>mayor:
        mayor=int(clave)
        nombre1=nombre

    total=total+int(clave)
    Contador+=1
print("el promedio de todos los puntajes es:",total/Contador)
print("el promedio mayor es: ",mayor,"y pertenece a:",nombre1)
#la cantidad total de jugadores

print("la cantidad total de jugadores es:",Contador)

