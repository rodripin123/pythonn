# Modulo: proyecto_innovaTC.py

from datetime import date


menu = {1:"Agregar",
        2:"Listado",
        3:"Consultar",
        4:"Eliminar",
        5:"Modificar",
        6:"Aumentar Stock",
        7:"Reducir Stock",
        8:"Compras",
        9:"Ventas",
        10:"Comprobante de Pago",
        11:"Salir"}

# Base de Datos:

cliente = {45878985:"Carlos Gómez Peralta",
           42236365:"Eliana Sanchez Campos",
           42121115:"Ruben Iglesias Santillan",
           45854589:"Celeste Ramos Isidro",
           47778987:"Lorena Fiestas Castillón"}

empleado = {100:"Ana Rosa Robles Quitana",
            200:"Carlos Guido Armendaris",
            300:"Fausto Peralta Altamirano",
            400:"Valentina Santa Alegre",
            500:"Roberto Campos Silva"}

carrito = {}
           
producto  = {1:"Arroz",2:"Azucar",3:"Fideos",4:"Avena",5:"Cerveza"}
precio = {1:4.0, 2:4.5, 3:1.5, 4:1.5, 5:8.0}
stock = {1:150, 2:100, 3:120, 4:80, 5:500}

# FUNCIONES

def leerProducto():
    return input("Ingrese Producto: ")

def leerPrecio():
    while (True):
        try:
            return float(input("Ingrese Precio: "))
        except:
            print("Error: el precio es invalido, vuelva intentar..")

def leerStock():
    while(True):
        try:
            return int(input("Ingrese Stock: "))
        except:
            print("Error: la cantidad es invalida, vuelva a intentar...")
            


def agregar():
    print()
    print("---------------------------------------------------")
    print("Agregar nuevos productos")
    print("---------------------------------------------------")
    a = len(producto) + 1
    producto[a] = leerProducto()
    precio[a] = leerPrecio()
    stock[a] = leerStock()
    print("Producto Agregado en almacen Satisfactoriamente..")
    print()

def listado():
    print()
    print("---------------------------------------------------")
    print("Listado de productos en almacen")
    print("---------------------------------------------------")
    for clave in producto:
        print(clave, producto[clave], precio[clave], stock[clave])
    print("Fin del Listado..... ")
    print()

def consultar():
    print()
    print("---------------------------------------------------")
    print("Consulta de productos en almacen")
    print("---------------------------------------------------")
    while (True):
        try:
            clave = int(input("Ingrese Clave a Consultar: "))
            break
        except:
            print("Error: la clave es invalidad, vuelva a intentar..")
        
    if (clave in producto):
        print()
        print("Clave       : ", clave)
        print("Producto    : ", producto[clave])
        print("Precio      : ", precio[clave])
        print("Stock       : ", stock[clave])
        print("Producto Encontrado....!")
        print()
    else:
        print()
        print("Producto no existe en almacen...!")
        print()
        
def aumentarStock():
    print()
    print("---------------------------------------------------")
    print("Aumentar Stocks de productos")
    print("---------------------------------------------------")
    while (True):
        try:
            clave = int(input("Ingrese Clave a Consultar: "))
            break
        except:
            print("Error: la clave es invalidad, vuelva a intentar..")
            
    if (clave in producto):
        print()
        print("Clave       : ", clave)
        print("Producto    : ", producto[clave])
        print("Precio      : ", precio[clave])
        print("Stock ------> ", stock[clave])
        print("Producto Encontrado....!")
        print()
        st = leerStock()
        stock[clave] += st
        print("Stock Actualizado....!")
        print()
    else:
        print()
        print("Producto no existe en almacen...!")
        print()

def reducirStock():
    print()
    print("---------------------------------------------------")
    print("Reducir Stocks de productos")
    print("---------------------------------------------------")
    while (True):
        try:
            clave = int(input("Ingrese Clave a Consultar: "))
            break
        except:
            print("Error: la clave es invalidad, vuelva a intentar..")
            
    if (clave in producto):
        print()
        print("Clave       : ", clave)
        print("Producto    : ", producto[clave])
        print("Precio      : ", precio[clave])
        print("Stock ------> ", stock[clave])
        print("Producto Encontrado....!")
        print()
        st = leerStock()
        stock[clave] -= st
        print("Stock Actualizado....!")
        print()
    else:
        print()
        print("Producto no existe en almacen...!")
        print()
    
def eliminar():
    print()
    print("---------------------------------------------------")
    print("Eliminar Productos en almacen")
    print("---------------------------------------------------")
    while (True):
        try:
            clave = int(input("Ingrese Clave a Consultar: "))
            break
        except:
            print("Error: la clave es invalidad, vuelva a intentar..")
            
    if (clave in producto):
        print()
        print("Clave -------> ", clave)
        print("Producto ----> ", producto[clave])
        print("Precio ------> ", precio[clave])
        print("Stock -------> ", stock[clave])
        print("Producto Encontrado....!")
        print()
        while(True):
            try:
                sw = int(input("¿Desea Eliminar? [1]Si, [2]No : "))
                break
            except:
                print("Error: opción incorrecta, debe escoger 1 o 2, vuelva a intentar")
                
        if (sw == 1):
            del producto[clave]
            del precio[clave]
            del stock[clave]
            print("Producto eliminado de almacen...!")
            print()
        else:
            print("No se realizó ninguna eliminación..")
            print()

    else:
        print()
        print("Producto no existe en almacen...!")
        print()
        
def modificar():
    print()
    print("---------------------------------------------------")
    print("Modificar Productos en almacen")
    print("---------------------------------------------------")
    while (True):
        try:
            clave = int(input("Ingrese Clave a Consultar: "))
            break
        except:
            print("Error: Clave incorrecta, vuelva a intentar")
            
    if (clave in producto):
        print()
        print("Clave -------> ", clave)
        print("Producto ----> ", producto[clave])
        print("Precio ------> ", precio[clave])
        print("Stock -------> ", stock[clave])
        print("Producto Encontrado....!")
        print()
        while(True):
            try:
                sw = int(input("¿Desea Eliminar? [1]Si, [2]No : "))
                break
            except:
                print("Error: opción incorrecta, debe escoger 1 o 2, vuelva a intentar")
                
        if (sw == 1):
            producto[clave] = leerProducto()
            precio[clave] = leerPrecio()
            stock[clave] = leerStock()
            print("Producto Modificar en almacen...!")
            print()
        else:
            print("No se realizó ninguna Modificación..")
            print()

    else:
        print()
        print("Producto no existe en almacen...!")
        print()
        

def ventas():
    print()
    print("---------------------------------------------------")
    print("Venta de Productos al Cliente")
    print("---------------------------------------------------")
    listado()
    clave = int(input("Selecciones clave del producto: "))
    if (clave in producto):
        can = int(input("Ingrese Cantidad: "))
        c = len(carrito) + 1 #genera clave automática
        carrito[c] = [producto[clave], precio[clave],can, precio[clave]*can]
    else:
        print("Error: El producto no existe....")
    
    print(carrito)

def comprobante():
    hoy = date.today()
    dni = int(input("Ingrese Dni: "))
    cod = int(input("Código de Empleado: "))
    print()
    print("---------------------------------------------------")
    print("Comprobante de Pago:")
    print("---------------------------------------------------")
    print("Ruc de la Empresa   :  10878569857")
    print("Fecha               : ", hoy)
    print("Cliente             : ", cliente[dni])
    print("Empleado            : ", empleado[cod])
    print("---------------------------------------------------")
    # Aqui se programa el detalle de carrito



# PROGRAMA PRINCIPAL
while (True):
    print()
    print("---------------------------------------------------")
    print("Menu Principal del Sistema:")
    print("---------------------------------------------------")
    for clave in menu:
        print(clave, menu[clave])
    print("---------------------------------------------------")
    while (True):
        try:
            op = int(input("Seleccione una opción: "))
            break
        except:
            print("Error: ingreso inválido, vuelva a intentar..")
            
    if (op == 1):
        agregar()
        
    elif (op == 2):
        listado()
        
    elif (op == 3):
        consultar()
        
    elif (op == 4):
        eliminar()
        
    elif (op == 5):
        modificar()
        
    elif (op == 6):
        aumentarStock()
        
    elif (op == 7):
        reducirStock()
        
    elif (op == 8):
        pass
    elif (op == 9):
        ventas()
        
    elif (op == 10):
        comprobante()
        
    elif (op == 11):
        print()
        print("Gracia por usar nuestra App...")
