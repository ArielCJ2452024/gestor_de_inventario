
from datetime import datetime


class producto:
    def __init__(self, id, nombre, precio, stock, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria



class proveedor:
    def __init__(self, rnc, nombre, telefono, correo):
        self.rnc = rnc
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo


class inventario:

    def __init__(self):
        self.productos = []
        self.historial = []
        self.proveedores = []

    def agregar_proveedor(self, proveedor):
        for p in self.proveedores:
            if p.rnc == proveedor.rnc:
                print("El proveedor ya existe en el inventario.")
                return False
        self.proveedores.append(proveedor)
        print("Proveedor agregado con éxito.")
        return True

    def eliminar_proveedor(self, rnc):
        for proveedor in self.proveedores:
            if proveedor.rnc == rnc:
                self.proveedores.remove(proveedor)
                print("Proveedor eliminado con éxito.")
                return True
        print("El proveedor no existe en el inventario.")
        return False

    def mostrar_proveedores(self):
        print("Lista de proveedores:")
        for proveedor in self.proveedores:
            print(f"RNC: {proveedor.rnc}, Nombre: {proveedor.nombre}, Teléfono: {proveedor.telefono}, Correo: {proveedor.correo}")

    def agregar_productos(self, producto):
        for p in self.productos:
            if p.id == producto.id:
                p.stock += producto.stock
                return True
        self.productos.append(producto)
        return True


    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id==id:
                self.productos.remove(producto)
                return True
        return False

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}, Categoria: {producto.categoria}")


    def registrar_venta(self, id, cantidad):
        for producto in self.productos:
            if producto.id == id:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    
                    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    transaccion = f"[{fecha_hora}] Venta: ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {cantidad}, Precio unitario: {producto.precio}, Total: {producto.precio * cantidad}"
                    self.historial.append(transaccion)

                    print("¡Venta registrada con éxito!")
                    return True
                else:
                    print("Error: No hay suficiente stock disponible.")
                    return False
        
        print("Error: El producto no existe en el inventario.")
        return False


    def alerta_stock(self, limite=5):
        print("Productos con stock bajo:")
        for producto in self.productos:
            if producto.stock < limite:
                print(f"alerta este producto tiene stock bajo: ID: {producto.id}, Nombre: {producto.nombre}, Stock: {producto.stock}")


    def mostrar_historial(self):
        print ("Historial de transacciones:")
        if not self.historial:
            print("No hay transacciones registradas.")
        else:
            for transaccion in self.historial:
                print(transaccion)


producto1 = producto(1, "Camiseta", 20.0, 50, "Ropa")

MI_inventario = inventario()
MI_inventario.agregar_productos(producto1)
MI_inventario.mostrar_productos()

venta_exitosa = MI_inventario.registrar_venta(1, 10)

historial = MI_inventario.mostrar_historial()
