


"""creacion de productos"""

class producto:
    def __init__(self, id, nombre, precio, stock, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria


class inventario:

    def __init__(self):
        self.productos = []

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





"""
(producto1 = producto(1, "Camiseta", 20.0, 50, "Ropa")

MI_inventario = inventario()
MI_inventario.agregar_productos(producto1)
MI_inventario.mostrar_productos()

"""
