"""
que reciba una cadena y 
verifique si cumple con los requisitos mínimos de una contraseña segura 
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras 
minúsculas, números y caracteres especiales). La función debe devolver un 
valor booleano que indique si la contraseña es válida o no
"""
import re
def validar_contrasena(contraseña):
    if len(contraseña)>8 and buscar_caracter_especial(contraseña) and buscar_numero(contraseña):
        return True

def buscar_caracter_especial(x):
    # Definir un patrón de caracteres especiales
    patron = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    
    # Buscar si hay coincidencias en la cadena
    if patron.search(x):
        return True
    else:
        return False
def buscar_numero(x):
    # Definir un patrón que busque cualquier dígito
    patron = re.compile(r'\d')
    
    # Buscar si hay coincidencias en la cadena
    if patron.search(x):
        return True
    else:
        return False
