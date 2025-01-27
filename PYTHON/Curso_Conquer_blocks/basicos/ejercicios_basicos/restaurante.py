print("esta es lalista de precios:\nEnsalada mixta ———————— 12 EU\nSopa de pescado ——————— 10 EU\nDorada al horno ———————— 18 EU\nArroz al curry ————————— 14 EU\nLasaña de carne ——————— 15 EU\nBrownie de chocolate ————— 8 EU\nHelado ——————————— 6 EU\nRefrescos —————————— 5,5 EU\nCafé ———————————— 3,5 EU")

print("que platos consumio")

Ensalada_mixta=12
Sopa_de_pescado=10
Dorada_al_horno=18
Arroz_al_curry=14
Lasaña_de_carne=15
Brownie_de_chocolate=8
Helado=6
Refrescos=float(5.5)
Cafe=float(3.5)
Ensalada_mixta1=float(input("cuantas ensaladas mixtas consumio: "))
Sopa_de_pescado1=float(input("cuantas sopas de pescado consumio: "))
Dorada_al_horno1=float(input("cuantas dorada al orno consumio: "))
Arroz_al_curry1=float(input("cuantas arroz con curry consumio: "))
Lasaña_de_carne1=float(input("cuantas lasaña de carne consumio: "))
Brownie_de_chocolate1=float(input("cuantas brownie de chocolate consumio: "))
helado1=float(input("cuantas helado consumio: "))
refresco1=float(input("cuantas refresco consumio: "))
cafe1=float(input("cuantas tasas de cafe consumio: "))
resutado=(Ensalada_mixta*Ensalada_mixta1)+(Sopa_de_pescado*Sopa_de_pescado1)+(Dorada_al_horno1*Dorada_al_horno)+(Arroz_al_curry1*Arroz_al_curry)+(Lasaña_de_carne1*Lasaña_de_carne)+(Brownie_de_chocolate1*Brownie_de_chocolate)+(helado1*Helado)+(refresco1*Refrescos)+(cafe1*Cafe)
print ("usted debe pagar(",resutado,"EU)")