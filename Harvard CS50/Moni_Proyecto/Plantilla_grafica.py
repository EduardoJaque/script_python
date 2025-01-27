import tkinter

def saludo():
    tkinter.Label(ventana, text="juguemos al #").pack()

def salir():
    ventana.destroy()

ventana = tkinter.Tk()
boton = tkinter.Button(ventana, text="1", command=saludo, fg="red")
boton.pack()
boton.place(x=200, y=200)

ventana.mainloop()

