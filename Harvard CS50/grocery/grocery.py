lista=[]
dic={}
def contador():
    for i in lista:
            dic[i]=lista.count(i)
    imprime()
def agregar():
    while True:
        try:
            x=input("").upper()
            lista.append(x)
        except (EOFError):
            lista.sort()
            contador()
            break
def imprime():
     for key, value in dic.items():
        print(f"{value} {key}")
agregar()


