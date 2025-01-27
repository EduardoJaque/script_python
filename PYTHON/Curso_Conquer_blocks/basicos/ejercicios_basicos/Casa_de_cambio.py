#casa de cambio 
euro=int(input("cuantos dolares quier cambiar: "))
dolar=euro*1.2
print(euro,"EU a dolar serian ",dolar,"$")
gestion= (dolar*0.10)
print("retencion por gestion: ", gestion, "$","\nrecibes:",dolar-gestion, "$" )