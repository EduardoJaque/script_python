import sys
import os
import csv
from tabulate import tabulate
def main():

    if len(sys.argv) ==2:
        nombre_archivo=sys.argv[1]
        extension = os.path.splitext(nombre_archivo)

        if extension!= ".csv":
            if extension==".txt":
                sys.exit("Not a CSV file")
            else:
                sys.exit("Not a CSV file")

        elif extension==".csv":

                if sys.argv[1]=="regular.csv" or sys.argv[1]=="sicilian.csv":
                    abrir_archivo(sys.argv[1])
                elif sys.argv[1]!="regular.csv" or sys.argv[1]!="sicilian.csv":
                    sys.exit("Not a CSV file")

    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too few command-line arguments")

def abrir_archivo(x):

    with open(x, 'r') as archivo:
        leer = csv.DictReader(archivo)
        datos = list(leer)

    tabla = tabulate(datos, headers="keys", tablefmt='grid')
    print (tabla)


if __name__=="__main__":
    main()