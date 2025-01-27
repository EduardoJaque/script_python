class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
class Tienda:
    def __init__(self):
        self.litsa_productos=[]

    def agregar(self,producto):
        self.litsa_productos.append(producto)
            
    def mostrar(self):
        for i in self.litsa_productos:
            print(f"producto {i.nombre} precio {i.precio} quedan {i.stock}")

    def comprar(self,producto,cantidad):
        for producto_comprar in self.litsa_productos:
            if producto_comprar.nombre==producto:
                if producto_comprar.stock>=cantidad:
                    print(f"si tenemos en stock\nsu precio es de {producto_comprar.precio}")
                    producto_comprar.stock-=cantidad
                    break
                else:
                    print(f"no tenemos {producto_comprar.nombre} en stock\nsolo nos quedan {producto_comprar.stock}")
                    break
        else:
            print(f"no tenermos {producto}")
            
tienda=Tienda() 
producto2=Producto("fideos",2000,5)
print()
tienda.agregar(producto2)
while True:
    pregunta=int(input("1.==> agregar producto:\n2.==> mostrar productos\n3.==> vender productos\n4.==> para salir\n")  )              
    if pregunta==1:
        nombre_producto=input("ingrese el nombre del producto: ")
        precio_producto=int(input("ingrese el precio del producto: "))
        cantidad_producto=int(input("ingrese la cantidad de productos: "))
        producto1=Producto(nombre_producto,precio_producto,cantidad_producto)
        tienda.agregar(producto1)
    elif pregunta==2:
        tienda.mostrar()
    elif pregunta==3:
        comprar_producto=input("que producto desea comprar: ")
        cantidad_de_producto=int(input("cuantos desea comprar: "))
        tienda.comprar(comprar_producto,cantidad_de_producto)
    elif pregunta==4:
        print("muchas gracias adios ")
        break
        






