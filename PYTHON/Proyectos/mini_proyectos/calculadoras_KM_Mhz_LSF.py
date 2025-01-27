import math

def calcular_LSF(KM, FM):
    return 32.44 + 20 * math.log10(KM) + 20 * math.log10(FM)

def calcular_KM(LSF, FM):
    return 10 ** ((LSF - 32.44 - 20 * math.log10(FM)) / 20)

def calcular_FM(LSF, KM):
    return 10 ** ((LSF - 32.44 - 20 * math.log10(KM)) / 20)

def calcular_DP(Ptx, Gtx, R):
    return (Ptx * Gtx) / (4 * math.pi * R ** 2)

def calcular_Ptx(DP, Gtx, R):
    return (DP * 4 * math.pi * R ** 2) / Gtx

def calcular_Gtx(DP, Ptx, R):
    return (DP * 4 * math.pi * R ** 2) / Ptx

def calcular_R(DP, Ptx, Gtx):
    return math.sqrt((Ptx * Gtx) / (4 * math.pi * DP))

def calcular_ZF(d1, d2, frecuencia, DT):
    ZF = 576 * math.sqrt((d1 * d2) / (frecuencia * DT))
    return ZF

def calcular_frecuencia(d1, d2, ZF, DT):
    frecuencia = (d1 * d2) / ((ZF / 576) ** 2 * DT)
    return frecuencia

def calcular_DT(d1, d2, ZF, frecuencia):
    DT = (d1 * d2) / ((ZF / 576) ** 2 * frecuencia)
    return DT
    
while True:
    print("¿Qué quieres hacer?")
    pregunta = int(input("1. LSF\n2. Kilómetros\n3. Frecuencia en MHz\n4. Densidad de potencia\n5. Potencia de transmisión\n6. Ganancia de transmisión\n7. Distancia R\n8. ZF\n9. frecuencia por ZF\n10. DT\n11. Salir\n"))

    if pregunta == 1:
        KM = float(input("Ingrese kilómetros en formato (2.5): "))
        FM = float(input("Ingrese la frecuencia en MHz: "))
        print("")
        print("")
        print(f":::::::::==========---------->>>>>>>>>>  |LSF = {calcular_LSF(KM, FM)}|  <<<<<<<<<<---------==========::::::::::")
        print("")
        print("")

    elif pregunta == 2:
        LSF = float(input("Ingrese LSF: "))
        FM = float(input("Ingrese la frecuencia en MHz: "))
        print(f"Kilómetros calculados: {calcular_KM(LSF, FM)}")

    elif pregunta == 3:
        LSF = float(input("Ingrese LSF: "))
        KM = float(input("Ingrese kilómetros en formato (2.5): "))
        print(f"Frecuencia en MHz calculada: {calcular_FM(LSF, KM)}")

    elif pregunta == 4:
        Ptx = float(input("Ingrese la potencia de transmisión en watts: "))
        Gtx = float(input("Ingrese la ganancia de la antena: "))
        R = float(input("Ingrese la distancia en metros: "))
        print(f"Densidad de potencia (DP): {calcular_DP(Ptx, Gtx, R)}")

    elif pregunta == 5:
        DP = float(input("Ingrese la densidad de potencia: "))
        Gtx = float(input("Ingrese la ganancia de la antena: "))
        R = float(input("Ingrese la distancia en metros: "))
        print(f"Potencia de transmisión (Ptx) calculada: {calcular_Ptx(DP, Gtx, R)}")

    elif pregunta == 6:
        DP = float(input("Ingrese la densidad de potencia: "))
        Ptx = float(input("Ingrese la potencia de transmisión en watts: "))
        R = float(input("Ingrese la distancia en metros: "))
        print(f"Ganancia de la antena (Gtx) calculada: {calcular_Gtx(DP, Ptx, R)}")

    elif pregunta == 7:
        DP = float(input("Ingrese la densidad de potencia: "))
        Ptx = float(input("Ingrese la potencia de transmisión en watts: "))
        Gtx = float(input("Ingrese la ganancia de la antena: "))
        print(f"Distancia (R) calculada: {calcular_R(DP, Ptx, Gtx)}")

    elif pregunta==8:
        frecuencia=float(input("Ingrese la frecuencia en MHz: "))
        DT=float(input("Ingrese kilómetros en formato (2.5): "))
        d1=float(input("ingrese D1: "))
        d2=float(input("ingrese D2: "))
        print(calcular_ZF(d1, d2, frecuencia, DT))
    elif pregunta==9:
        d1=float(input("ingrese D1: "))
        d2=float(input("ingrese D2: "))
        DT=float(input("Ingrese kilómetros en formato (2.5): "))
        ZF=float(input("ingrese ZF: "))
        print(calcular_frecuencia(d1, d2, ZF, DT))
    elif pregunta==10:
        d1=float(input("ingrese D1: "))
        d2=float(input("ingrese D2: "))
        ZF=float(input("ingrese ZF: "))
        frecuencia=float(input("Ingrese la frecuencia en MHz: "))
        print(calcular_DT(d1, d2, ZF, frecuencia))
    elif pregunta == 11:
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 8.")
        


"""
# Ejemplo de uso:
KM = 10  # Distancia en kilómetros
FM = 100  # Frecuencia en MHz

LSF = calcular_LSF(KM, FM)
print(f"LSF: {LSF}")

LSF = 100  # Ejemplo de LSF
KM_calculado = calcular_KM(LSF, FM)
print(f"KM calculado: {KM_calculado}")

FM_calculado = calcular_FM(LSF, KM)
print(f"FM calculado: {FM_calculado}")


# Ejemplo de uso:
Ptx = 50  # Potencia de transmisión en watts
Gtx = 2  # Ganancia de la antena
R = 10  # Distancia en metros

DP = calcular_DP(Ptx, Gtx, R)
print(f"Densidad de potencia (DP): {DP}")

DP = 0.1  # Ejemplo de densidad de potencia
Ptx_calculado = calcular_Ptx(DP, Gtx, R)
print(f"Potencia de transmisión (Ptx) calculada: {Ptx_calculado}")

Gtx_calculado = calcular_Gtx(DP, Ptx, R)
print(f"Ganancia de la antena (Gtx) calculada: {Gtx_calculado}")

R_calculado = calcular_R(DP, Ptx, Gtx)
print(f"Distancia (R) calculada: {R_calculado}")
"""
