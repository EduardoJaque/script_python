#explicar que es esto
print("esta es una calculadora de ahorros anuales")
#pedir nombre a persona y saludar
nombre=input("cual es tu nombre: ")
print("hola", nombre)
#pedir horas trabajadas, ganancia por hora, gastos 
ganacia=int(input("puedes indicar cuanto ganas por hora: "))
horas=int(input("cuantas horas trabajas a la semana: "))
gastos=int(input("puedes indicar cuanto gastas a la semana: "))
#calcular salario semanal
salario_semanal=ganacia*horas-gastos
salario_anual=salario_semanal*52
total=((ganacia*horas)*52)-salario_anual
print("tus ahorros pueden ser de:",salario_anual)
print("tu salario anual es de: ",total)
print((gastos*52)-salario_anual)


