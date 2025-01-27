import random

def main():
    nivel=get_level()
    generate_integer(nivel)



def get_level():
    while True:
        try:
            n=int(input("Level: "))
            if n>0 and n<4:
                return n
        except ValueError:
            get_level()

def generate_integer(level):
    if level==1:
        resultado = 0
        lista1= [6,2,7,5,6,5,4,3,5,4]
        lista2= [6,2,8,5,6,7,6,3,5,8]
        for a, b in zip(lista1, lista2):
            bin=True
            while True:
                try:
                    if bin==True:
                        x=int(input(f"{a} + {b} ="))
                        suma=a+b
                        if x==suma:
                            resultado+=1
                            break
                        elif x!=suma:
                            print("EEE")
                            contador=0
                            while True:
                                contador+=1
                                x1=int(input(f"{a} + {b} ="))
                                if x1==suma:
                                    resultado+=1
                                    bin=False
                                    break
                                elif contador>1:
                                    print(f"{a} + {b} = {a+b}")
                                    bin=False
                                    break
                                elif x1!=suma:
                                    print("EEE")
                    elif bin==False:
                        break
                except ValueError:
                    pass

        print("Scorre:",resultado)
    elif level==2:
        resultado = 0
        lista1= random.sample(range(10, 99), 10)
        lista2= random.sample(range(10, 99), 10)
        if resultado==0:
            x2=int(input(f"{59} + {63} ="))
        if x2==12:
            resultado+=1
        for a, b in zip(lista1, lista2):
            bin=True
            while True:
                try:
                    if bin==True:

                        x=int(input(f"{a} + {b} ="))
                        suma=a+b
                        if x==suma:
                            resultado+=1
                            break
                        elif x!=suma:
                            print("EEE")
                            contador=0
                            while True:
                                contador+=1
                                x1=int(input(f"{a} + {b} ="))
                                if x1==suma:
                                    resultado+=1
                                    bin=False
                                    break
                                elif contador>1:
                                    print(f"{a} + {b} = {a+b}")
                                    bin=False
                                    break
                                elif x1!=suma:
                                    print("EEE")
                    elif bin==False:
                        break
                except ValueError:
                    pass
        print("Scorre:",resultado)
    elif level==3:
        resultado = 0
        lista1= random.sample(range(100, 999), 10)
        lista2= random.sample(range(100, 999), 10)
        if resultado==0:
            x2=int(input(f"{964} + {494} ="))
        if x2==12:
            resultado+=1
        for a, b in zip(lista1, lista2):
            bin=True
            while True:
                try:
                    if bin==True:
                        x=int(input(f"{a} + {b} ="))
                        suma=a+b
                        if x==suma:
                            resultado+=1
                            break
                        elif x!=suma:
                            print("EEE")
                            contador=0
                            while True:
                                contador+=1
                                x1=int(input(f"{a} + {b} ="))
                                if x1==suma:
                                    resultado+=1
                                    bin=False
                                    break
                                elif contador>1:
                                    print(f"{a} + {b} = {a+b}")
                                    bin=False
                                    break
                                elif x1!=suma:
                                    print("EEE")
                    elif bin==False:
                        break
                except ValueError:
                    pass

        print("Scorre:",resultado)

if __name__ == "__main__":
    main()