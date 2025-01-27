from PIL import Image, ImageOps
import os
import sys

def main():
    if len(sys.argv)==3:

        if validar(sys.argv[1]) and corroborar (sys.argv[2],['.jpg', '.png', '.txt']):
            abrir(sys.argv[1],sys.argv[2])

    elif len(sys.argv)!=3:
        sys.exit()

def validar(X):
    x= X.lower()
    ruta="/workspaces/131680858/shirt"
    for archivo in os.listdir(ruta):
        if archivo == x:
            return True
    return False

def corroborar(nombre_archivo, extensiones_validas):
    nombre_archivo1 = nombre_archivo.lower()
    extension_archivo = os.path.splitext(nombre_archivo1)
    if extension_archivo[1] in extensiones_validas:
        return True
    return False

def abrir(x,i):
    # Crea una nueva imagen con un tamaño y color de fondo específicos
    final = Image.new("RGBA", (1920, 1065), (0,0,0,252))

# Abre las imágenes que quieres pegar
    imagen1 = Image.open("ruta/a/imagen1.png")
    imagen2 = Image.open("ruta/a/imagen2.png")

# Pega las imágenes en la imagen final en las posiciones (x, y) especificadas
    final.paste(imagen1, (150,100))
    final.paste(imagen2, (0,0))

# Muestra y guarda la imagen final
    final.show()
    final.save("ruta/a/imagen/final.png")
    x1= Image.open('/workspaces/131680858/shirt/'+x)
    size=(1200,1600)
    nueva_imagen= ImageOps.fit(x1, size, Image.LANCZOS)
    nueva_imagen.save('/workspaces/131680858/shirt/'+i)

if __name__=="__main__":
    main()