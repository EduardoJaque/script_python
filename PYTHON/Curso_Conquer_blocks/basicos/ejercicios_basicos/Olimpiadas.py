print("Ingrese el tiempo del primer finalista")
min_primero = int(input("minutos:"))
seg_primero = int(input("segundos:"))
cen_primero = int(input("centesimas:"))

min_primero=min_primero*60
cen_primero=cen_primero/100
primero=round(100/(min_primero+seg_primero+cen_primero),2)
print("ingrese el tiempo del segundo finalista:")
min_segundo = int(input("minutos:"))
seg_segundo = int(input("segundos:"))
cen_segundo = int(input("centesimas:"))

min_segundo=min_segundo*60
cen_segundo=cen_segundo/100
segundo=round(100/(min_segundo+seg_segundo+cen_segundo),2)

print("ingrese el tiempo del tercer finalista:")
min_tercer = int(input("minutos:"))
seg_tercer = int(input("segundos:"))
cen_tercer = int(input("centesimas:"))

min_tercer=min_tercer*60
cen_tercer=cen_tercer/100
tercer=round(100/(min_tercer+seg_tercer+cen_tercer),2)

print("la velocidad media de los finalista son:\nprimer finalista ingresado:",primero,"m/s\nsegundo finalista ingresado:",segundo,"m/s\ntercer finalista ingresado:",tercer,"m/s")

#8 minutos 12 segundos 12 centesimas