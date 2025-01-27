dict={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def preguntar():
    while True:
            try:
                item=input("Item: ").title()
                if item in dict:
                     return item
            except (KeyError,AttributeError):
                 pass
def sumar():
    contador=0
    while True:
            try:
                x=preguntar()
                x1=float(dict[x])
                contador+=x1
                print("${:.2f}".format(contador))

            except (EOFError):
                 print("\n")
                 break

sumar()