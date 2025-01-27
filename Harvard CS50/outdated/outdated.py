meses=["January","February","March","April","May","June","July","August","September","October","November","December"]
def entrada():
    try:
        x=input("Date: ")
        x1=x.find(",")
        x2=x.find("/")
        if x1 >0 and x2>0 or x1<0 and x2<0:
            entrada()
        elif x1>0:
            orden2(x)
        elif x2>0:
            orden(x)
    except (EOFError):
        print("\n")
def orden(x):
    try:
        M,D,Y=x.split("/")
        M=int(M)
        if M>12:
            entrada()
        D=int(D)
        if D >31:
            entrada()
        Y=int(Y)
        print(f"{Y}-{M:02}-{D:02}")
    except (IndexError,ValueError):
        entrada ()
def orden2(x):
    try:
        x=x.title()
        x=x.replace(",","")
        M,D,Y=x.split(" ")
        D=int(D)
        if D>31:
            entrada()
        Y=int(Y)
        contador=1
        for j in meses:
            if j!=M:
                contador+=1
            if j==M:
                break
        M=contador
        print(f"{Y}-{M:02}-{D:02}")

    except (IndexError,ValueError):
        entrada()
entrada()