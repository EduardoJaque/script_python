"""REGISTRO DE VENTAS: 
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias 
de tus productos. Cada producto tiene un nombre y una cantidad 
vendida. Implementa un programa en Python que utilice un diccionario 
para almacenar la información de las ventas. El programa debe permitir 
registrar las ventas de productos, actualizar la cantidad vendida de un 
producto existente y calcular el total de ventas diarias.
 (Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada 
producto)"""

ventas_diarias={"arroz":2}
#bucle para seguir preguntando
while True:
    # pedir nombre de producto 

    venta=input("ingrese el producto:")
    cantidad=int(input("ingrese cantidad:"))

    # verificar si se ha vendido # agregar o modificar
    if ventas_diarias.get(venta,False)==False:
        ventas_diarias[venta]=cantidad
    elif ventas_diarias.get(venta):
        suma=int(ventas_diarias.get(venta))
        suma=suma+cantidad
        ventas_diarias[venta]=suma
    print(ventas_diarias)

    terminar=input("quieres terminar: ").title()
    # preguntar si quiere parar
    if terminar=="Si":
        break
    else:
        continue


 
