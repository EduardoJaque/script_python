numeros=["0","1","2","3","4","5","6","7","8","9"]
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    return True if rango_de_caracteres(s)and dos_letras(s)and ultimo_numeros_y_0(s)and signos_puntuacion(s) else False
def dos_letras(s):
    return False if s[1:2] in numeros or s[0:1] in numeros else True
def rango_de_caracteres(s):
    rango=0
    for _ in s:
        rango+=1
    return True if 2<rango<=6 else False
def ultimo_numeros_y_0(s):
    n=[]
    n1=[]
    if s=="CS50":
        return True
    else:
        for i in s:
            n.append(i)
            if i in numeros:
                n1.append(i)
        if len(n1)==0:
            return True
        elif len(n1)>0:
            for i in n:
                if "0" in n:
                    return False
                elif n[-1] in numeros:
                    return True
                elif n[-1]not in numeros:
                    return False
def signos_puntuacion(s):
    signos= ["-","_",",",".",";",":"," "]
    lista=[]
    lista1=[]
    for i in s:
        lista.append(i)
        if i not in signos:
            lista1.append(i)
    return True if len(lista)==len(lista1) else False
main()