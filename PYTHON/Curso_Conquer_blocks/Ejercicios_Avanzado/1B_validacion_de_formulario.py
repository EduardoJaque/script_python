"""Crea un programa que valide un formulario de registro. Crea una función 
llamada validar_formulario que reciba diferentes campos de un formulario 
(nombre, correo electrónico y número de teléfono) y verifique si los valores 
ingresados cumplen con los requisitos especificados, siendo estos:
 1. Que el nombre tenga una longitud minima de 3 caracteres
 2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 
caracteres
 3. Que el email contenga un “@“ y un “.”"""
#Crea una función llamada validar_formulario
boleano=True
def validar_formulario(nombre,correo,numero):
   
    if len(nombre)>3 and isinstance(numero, int) and correo.find(".")!=-1 and correo.find("@")!=-1:
        return True
         
def main():
    
    while boleano:
        nombre=input("ingrese su nombre: ")
        correo=input("ingrese su correo: ")
        numero=int(input("ingrese su numero telefonico: "))
        if validar_formulario(nombre,correo,numero):
            print("datos validos")
        else:
            print("datos invalidos")
if __name__ == "__main__":
    main()


