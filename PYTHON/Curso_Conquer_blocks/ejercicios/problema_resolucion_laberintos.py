#Problema de Resolución de Laberinto:
"""
Imagina que eres parte de un equipo de desarrollo de IA que se encarga de
crear un sistema para que un robot resuelva laberintos. El laberinto está
representado por una matriz, donde ciertos valores indican caminos permitidos
( 0 ), paredes ( 1 ), y la salida ( 9 ). Tu tarea es implementar una función
recursiva que encuentre la ruta más corta para que el robot salga del laberinto.
Toma en cuenta los siguientes puntos:
1. La matriz representa el laberinto, donde los valores son:
0 : Camino permitido.
1 : Pared, no se puede atravesar.
9 : Salida del laberinto.
2. Debes implementar la función resolver_laberinto que utiliza recursividad
para encontrar la ruta más corta desde una posición inicial hasta la salida.
3. La función debe devolver una lista de coordenadas que representan la ruta
desde la posición inicial hasta la salida.
4. Puedes usar una lista de movimientos posibles: arriba ( (-1, 0) ), abajo( (1,
0) ), izquierda ( (0, -1) ), derecha ( (0, 1) ).
A continuacion un ejemplo de una posible entrada y salida de la solucion:

"""

