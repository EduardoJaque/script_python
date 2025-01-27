#Juego de Arcade Pong
"""
Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para 
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los 
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los 
controles del usuario para las paletas de los jugadores izquierda y derecha.
"""
import turtle

# Crear una ventana de dibujo
ventana = turtle.Screen()

# Crear una tortuga
mi_tortuga = turtle.Turtle()

# Dibujar un cuadrado
for _ in range(4):
    mi_tortuga.forward(100)  # Mover hacia adelante 100 unidades
    mi_tortuga.right(90)     # Girar 90 grados a la derecha

# Cerrar la ventana al hacer clic
ventana.exitonclick()
