#‘’'\n
#Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
#Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’

#recibir el string
entrada="David Fernandez 12311267A 43527 2 9.1 7.6 2.4"

#agregarlo a la lista y separar
lista=entrada.split()
#manejar los ultimos tres elementos (notas)
ultimos_tres = list(map(float, lista[-3:]))
# Calcular el promedio de los últimos tres elementos

promedio=round(sum(ultimos_tres) / len(ultimos_tres),2)
DNI=lista[2]
#dvolver lo solicitado 
print (f"el DNI {DNI}tubo una nota de {promedio}")


