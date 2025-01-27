"""
que genere contraseñas seguras de forma aleatoria. La 
función debe permitir especificar la longitud de la contraseña y qué tipos de 
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras 
minúsculas, números y caracteres especiales). (Para el generador de contraseñas puedes probar a usar los modulos 
random y string"
"""
import random
import string
def generar_contrasena(contraseña):
    caracter_especial = random.choice(string.punctuation) #genera un caracter especial aleatorio
    caracter_extra = random.choice(string.ascii_lowercase)#genera una letra mayuscula aleatoria
    palabra=contraseña.title()
    numero_aleatorio=str(random.randint(1, 100))

    nueva_contraseña=caracter_especial+palabra+numero_aleatorio+caracter_extra+caracter_especial
    return nueva_contraseña

