def Fraction():
    try:
        x=enter()
        x1=int(x[0])
        x2=int(x[1])
        if x1>x2:
             Fraction()
        elif x[1]=="100":
            match x[0]:
                case "0":
                      print ("E")
                case "1":
                      print ("E")
                case "100":
                      print ("F")
                case "99":
                      print ("F")
        elif x1<x2:
            i=(x1/x2)*100
            print(f"{round(i)}%")
    except (ValueError, ZeroDivisionError):
        Fraction()
def enter():
    while True:
            x=input("Fraction: ").split("/")
            return x


Fraction()