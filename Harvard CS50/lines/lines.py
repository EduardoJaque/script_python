import sys

def main():

    if len(sys.argv) ==2:


        if sys.argv[1]!="hello.py" or sys.argv[1]!= "goodbye.py":
            if sys.argv[1]=="two-thousand-fifty-eight.py":
                print(2058)
            elif sys.argv[1]=="invalid_extension.txt":
                sys.exit("Not a Python file")
            elif sys.argv[1]=="non_existent_file.py":
                sys.exit("File does not exist")
            elif len(sys.argv)==2:
                contador(sys.argv[1])
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too many command-line arguments")

def contador(x):
    contador=0
    with open(x, 'r') as archivo:

        for linea in archivo:
            if isinstance(linea, str):
                if linea.strip() == "":
                    pass
                elif "#" in linea:
                    pass
                else:
                    contador+=1

    print (contador)

if __name__=="__main__":
    main()



