import sys
import csv
import os
import pandas as pd

def main():
    if len(sys.argv) <2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >=4:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)>=2:
        abrir(sys.argv[1]) if  buscar_archivo(sys.argv[1])==True else sys.exit("Could not read "+sys.argv[1])
        exit(0)
def buscar_archivo(x):
    ruta="/workspaces/131680858/scourgify"
    for archivo in os.listdir(ruta):
        if archivo == x:
            return True
    return False

def abrir(y):
    ruta="/workspaces/131680858/scourgify/"+y
    df = pd.read_csv(ruta)

    df[['last', 'first',]] = df['name'].str.split(' ', expand=True)
    df = df.drop(columns=['name'])
    df = df[['first','last','house' ]]
    df_ordenado = df.sort_values(['first','last'])
    r="/workspaces/131680858/scourgify/"+sys.argv[2]
    df_ordenado.to_csv(r, index=True)
    exit(0)

if __name__=="__main__":
    main()


