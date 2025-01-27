"""Crea un script que solicite una contraseña, analice si es segura y si no lo es 
sugiera una nueva contraseña. Para ello puedes crear un script validador.py 
que contenga una funcion validar_contrasena que reciba una cadena y 
verifique si cumple con los requisitos mínimos de una contraseña segura 
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras 
minúsculas, números y caracteres especiales). La función debe devolver un 
valor booleano que indique si la contraseña es válida o no. Por otro lado 
puedes crear otro script creador.py con una función llamada 
generar_contrasena que genere contraseñas seguras de forma aleatoria. La 
función debe permitir especificar la longitud de la contraseña y qué tipos de 
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras 
minúsculas, números y caracteres especiales).
 (Para el generador de contraseñas puedes probar a usar los modulos 
random y string"""
import creador 
import validador
#cilco para mantener el programa
while True:
    #Crea un script que solicite una contraseña
    print("1. validar contraseña\n2. generar contraseña")
    pregunta=int(input("***seleccione una opcion*** \n "))

    if pregunta==1:
        #analice si es segura y 
        contraseña=input("ingrese una contraseña: ")
        if validador.validar_contrasena(contraseña):
            print("la contraseña es valida y segura")
        else:
            #si no lo es sugiera una nueva contraseña.
            print(f"se suguiere la contraseña\n ||==> {creador.generar_contrasena(contraseña)} <==||")
    elif pregunta==2:
        contraseña=input("suguiera una palabra clave: ")

        print(f"se suguiere la contraseña\n ||==> {creador.generar_contrasena(contraseña)} <==||")
    elif pregunta==3:
        break
    else:
        print("opcion invalida")