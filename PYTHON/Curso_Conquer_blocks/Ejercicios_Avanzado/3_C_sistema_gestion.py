"""
SISTEMA DE GESTIÓN DE EMPLEADOS
Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.

- Clase base: `Empleado`
 - Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
 - Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
 - Atributo adicional: horas trabajadas por semana

 Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados.
"""

class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre=nombre
        self.apellido=apellido
        self.salario=salario
    
class EmpleadoTiempoCompleto(Empleado):

    def __init__(self,nombre,apllido,salario,bono):
        super().__init__(nombre,apllido,salario)
        self.bono_anual=bono

    def calcularSalarioCompleto(self):
        print( f"el salario de {self.nombre} {self.apellido} es de {self.salario+self.bono_anual}")
        print(f"donde el bono es de {self.bono_anual}\ny el salario es de {self.salario}")


class EmpleadoTiempoParcial(Empleado):

    def __init__(self,nombre,apllido,salario,horas):
        super().__init__(nombre,apllido,salario)
        self.Horas_trabajadas_semana=horas

    def CalcularSalarioParcial(self,horas):
        print( f"el salario de {self.nombre} {self.apellido} es de {self.salario+self.Horas_trabajadas_semana}")
        print(f"donde el salario base es de {self.salario} por hora\ny trabajo {self.Horas_trabajadas_semana}")
    
    

empleado_parcial=EmpleadoTiempoParcial("juanito","jake",500,5)
empleadoTiempoCompleto=EmpleadoTiempoCompleto("eduardo","jake",500,100)
#empleado_parcial=EmpleadoTiempoParcial()

#empleado_parcial.CalcularSalarioParcial(5)
empleadoTiempoCompleto.calcularSalarioCompleto()
empleado_parcial.CalcularSalarioParcial()
