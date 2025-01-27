import sys
from pyfiglet import Figlet
import random

def atributo():
    if len(sys.argv)==1:
        letra_aleatorio()
    elif len(sys.argv)>=2:
        if len(sys.argv)==2:
            sys.exit("Invalid usage")
        elif sys.argv[0]=="figlet.py" and sys.argv[1]=="--front":
            sys.exit("Invalid usage")
        elif sys.argv[1]=="-f" or sys.argv[1]=="--font":
            tipo_letra()
        elif sys.argv[1]!="-f" or sys.argv[1]!="--font":
            sys.exit("Invalid usage")

        else:
            letra_aleatorio()

def letra_aleatorio():
    inpu=input("Input:")
    figlet = Figlet()
    figfonts = figlet.getFonts()
    f=random.choice(figfonts)
    figlet.setFont(font=f)
    print("Output: ")
    print(figlet.renderText(inpu))

def validar(x):
    figlet = Figlet()
    figfonts = figlet.getFonts()
    return True if x in figfonts else False

def tipo_letra():
    if validar(sys.argv[2]):
        inpu=input("Input:")
        f = Figlet(font=sys.argv[2])
        print("Output: ")
        print(f.renderText(inpu))
    else:
        sys.exit("Invalid usage")


if __name__=="__main__":
        atributo()


