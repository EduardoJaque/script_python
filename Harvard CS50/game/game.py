import random
def nivel():
    while True:
        try:
            n=int(input("Level: "))
            if n>0:
                return n
        except ValueError:
            nivel()

def guess():
    while True:
        try:
            n1=int(input("Guess: "))
            if n1>0:
                return n1
        except ValueError:
            guess()

def numero_random():
    try:

        numero=random.randint(1,x)
        return numero
    except TypeError:
        nivel()

def pregunta():
    x1=numero_random()
    while True:
        x2=guess()
        if x2==x1:
            print("Just right!")
            break
        elif x2>x1:
            print("Too large!")
        elif x2<x1:
            print("Too small!")

x=nivel()

if __name__=="__main__":
    pregunta()



