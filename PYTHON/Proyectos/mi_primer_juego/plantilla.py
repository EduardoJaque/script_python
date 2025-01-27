import tkinter
import Game
turnos= 1
def saludo(boton):
    Game.info_lista2.append(int(boton))
    # Cambiar el texto del botón a 'O' o 'X' cuando se presione
    cambiar (int(boton))
    etiqueta = tkinter.Label(ventana, text=f"Botón {boton} presionado")
    etiqueta.place(x=40, y=10)

def ganador(boton):
    print(f"el ganador es {boton}")

def cambiar(x):
    if x == 1:
        boton1.config(text='O')
        Game.insertar_numero(0, 0, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
      
    elif x ==2:
        boton2.config(text='O')
        Game.insertar_numero(0, 1, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        
    elif x ==3:
        boton3.config(text='O')
        Game.insertar_numero(0, 2, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        
    elif x ==4:
        boton4.config(text='O')
        Game.insertar_numero(1, 0, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        
    elif x ==5:
        boton5.config(text='O')
        Game.insertar_numero(1, 1, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        
    elif x ==6:
        boton6.config(text='O')
        Game.insertar_numero(1, 2, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        
    elif x ==7:
        boton7.config(text='O')
        Game.insertar_numero(2, 0, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        
    elif x ==8:
        boton8.config(text='O')
        Game.insertar_numero(2, 1, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        
    elif x ==9:
        boton9.config(text='O')
        Game.insertar_numero(2, 2, 2)
        Game.verificar_ganador(Game.info_lista)
        Game.moderador()
        

def cambiarx(x):
    if x == 1:
        boton1.config(text='X')
        Game.insertar_numero(0, 0, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==2:
        boton2.config(text='X')
        Game.insertar_numero(0, 1, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==3:
        boton3.config(text='X')
        Game.insertar_numero(0, 2, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==4:
        boton4.config(text='X')
        Game.insertar_numero(1, 0, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==5:
        boton5.config(text='X')
        Game.insertar_numero(1, 1, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==6:
        boton6.config(text='X')
        Game.insertar_numero(1, 2, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==7:
        boton7.config(text='X')
        Game.insertar_numero(2, 0, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==8:
        boton8.config(text='X')
        Game.insertar_numero(2, 1, 1)
        Game.insertar_numeros_maquina(x)
    elif x ==9:
        boton9.config(text='X')
        Game.insertar_numero(2, 2, 1)
        Game.insertar_numeros_maquina(x)

def salir():
    ventana.destroy()

ventana = tkinter.Tk()
ventana.geometry('180x180')
etiqueta = tkinter.Label(ventana, text="elige un nivel")
etiqueta.place(x=60, y=10)

def eliminar_boton(boton):
    boton.destroy()

def cambiar_nivel(x):
    Game.dificultad=int(x)
    if x == '1':
        facil.config(text='facil')
        facil.place(x=80,y=50)
        eliminar_boton(dificil)
        eliminar_boton(medio)
        boton_pack()
        Game.moderador()
        
    elif x =='2':
        medio.config(text='medio')
        medio.place(x=80,y=50)
        eliminar_boton(facil)
        eliminar_boton(dificil)
        boton_pack()
        Game.moderador()
        
    elif x =='3':
        dificil.config(text='dificil')
        dificil.place(x=80,y=50)
        eliminar_boton(facil)
        eliminar_boton(medio)
        boton_pack()
        Game.moderador()
        
# Crear los botones DE DIFICULTAD
facil = tkinter.Button(ventana, text="facil", command=lambda: cambiar_nivel('1'), fg="blue")
facil.pack()
facil.place(x=40, y=50)
medio = tkinter.Button(ventana, text="medio", command=lambda: cambiar_nivel('2'), fg="blue")
medio.pack()
medio.place(x=80, y=50)
dificil = tkinter.Button(ventana, text="dificil", command=lambda: cambiar_nivel('3'), fg="blue")
dificil.pack()
dificil.place(x=130, y=50)
#muestra los botones ocultos 
def boton_pack():
    boton1.place(x=48, y=80)
    boton2.place(x=95, y=80)
    boton3.place(x=140, y=80)
    boton4.place(x=48, y=110)
    boton5.place(x=95, y=110)
    boton6.place(x=140, y=110)
    boton7.place(x=48, y=140)
    boton8.place(x=95, y=140)
    boton9.place(x=140, y=140)
   
# Crear los botones DEL 1 AL 9
boton1 = tkinter.Button(ventana, text="1", command=lambda: saludo('1'), fg="red")
boton2 = tkinter.Button(ventana, text="2", command=lambda: saludo('2'), fg="red")
boton3 = tkinter.Button(ventana, text="3", command=lambda: saludo('3'), fg="red")
boton4 = tkinter.Button(ventana, text="4", command=lambda: saludo('4'), fg="red")
boton5 = tkinter.Button(ventana, text="5", command=lambda: saludo('5'), fg="red")
boton6 = tkinter.Button(ventana, text="6", command=lambda: saludo('6'), fg="red")
boton7 = tkinter.Button(ventana, text="7", command=lambda: saludo('7'), fg="red")
boton8 = tkinter.Button(ventana, text="8", command=lambda: saludo('8'), fg="red")
boton9 = tkinter.Button(ventana, text="9", command=lambda: saludo('9'), fg="red")






