import random
import plantilla
import sys
# falta no cambiar a o las jugadas de x
# nivel dificil
# mensaje en pantalla de quien gano 
# boton de volver a jugar 
dificultad='0'
info_lista = [0, 0, 0],[0, 0, 0],[0, 0, 0]
repetir=0
info_lista2 = []
jugadas_medio=[1,2,3,6,9,8,7,4]
jugadas_dificil=[5,3,7,7,3,5,9,1,5,1,9,5,4,6,5,6,4,5,2,8,5,8,2]




def abrirventana():
    plantilla.ventana.mainloop()

def moderador():
    
    turno_maquina()  
    #juega maquina
    if verificar_ganador(info_lista) ==0:
        print(verificar_ganador(info_lista))
        print("sin ganador")
              
    elif verificar_ganador(info_lista)== 2 or 1:
        print(verificar_ganador(info_lista))
        if verificar_ganador(info_lista)==2:
            print(verificar_ganador(info_lista))
            plantilla.ganador("O")
            
            sys.exit()
        elif verificar_ganador(info_lista)==1:
            print(verificar_ganador(info_lista))
            plantilla.ganador("X")
            
            sys.exit()

#con ayuda de buscar numero, revisa si esta el numero en la lista    
def revisar(x):
    repetir=+1
    if buscar_numero(x):
        plantilla.cambiarx(x)
        
    elif repetir>9:
        sys.exit()
    else:

        turno_maquina()            
    
# busca el nuero en la lista
def buscar_numero (x):
    for i in info_lista2:
        if i == x:
        
            return False
                
    return True

#insertar numeros de la persona en el tablero        
def insertar_numero(fila,columna,numero):
    info_lista[fila][columna] = numero
    
def insertar_numeros_maquina(x):
    info_lista2.append(x)

def turno_maquina():
    if repetir>9:
        sys.exit()
    elif dificultad== 1:
        facil()
    elif dificultad==2:
        medio()
    elif dificultad==3:
       next(mi_generador)

# genera numero del 1 al 9
def facil():
    maquina=random.randint(1, 9)
    revisar(int(maquina))

#jugada nivel medio 
def medio():

    jugada= jugadas_medio[0]
    jugadas_medio.remove(jugadas_medio[0])
        
    revisar(int(jugada))

def dificil(lista):
    print(lista)
    for numero in lista:
        yield revisar(int(numero))


mi_generador = dificil(jugadas_dificil)
def verificar_ganador(tablero):
    
    # Verificar filas
    for fila in tablero:
        if fila.count(fila[0]) == len(fila) and fila[0] != 0:
           
            return fila[0]

    # Verificar columnas
    for col in range(len(tablero)):
        columna = [fila[col] for fila in tablero]
        if columna.count(columna[0]) == len(columna) and columna[0] != 0:
            
            return columna[0]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != 0:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != 0:
        return tablero[0][2]

    return 0  # No hay ganador



if __name__ == "__main__":
    abrirventana()
    