"""Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento."""
import numpy as np
diccionario={'Jake': ['500', 'A'], 'Anna': ['600', 'A'], 'Tom': ['700', 'B']}
lista=[]
#agregar nuevos empleados
boleano=True
while boleano:
    empleado=input("ingrese nuevo empleado: ").title()
    salario=input("ingrese el salario: ")
    lista.append(salario)
    departamento=input("ingrese el departamento: ")
    lista.append(departamento)
    diccionario[empleado]=lista
    continuar=input("¿desea contunar?").title()
    if continuar=="N":
        boleano=False

#actualizar el salario de un empleado existente
pregunta=input("desea actualizar el salario de un empleado: ").title()
if pregunta=="S":
    empleado=input("indique el empleado: ").title()
    suma=input("ingrese el nuevo salario: ")
    diccionario[empleado][0]=suma

#mostrar la lista completa de empleados
print("los empleados son:",diccionario.keys())
#calcular el promedio salarial por departamento
suma_A=0
suma_B=0
for nombre, lista in diccionario.items():
    numero = int(lista[0])  # Convertir el número a entero
    letra = lista[1]
    
    if letra == 'A':
        suma_A += numero
        letra1 = lista[1]
    elif letra == 'B':
        suma_B += numero
        letra2 = lista[1]
        
print(f"la suma del departamento {letra1} es {suma_A}\nla suma del departamento {letra2} es {suma_B}")