class Cliente:
    def __init__(self, nombre, apellido, email, domicilio):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.domicilio = domicilio

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nEmail: {self.email}\ndomicilio: {self.domicilio}"

class LocalCompras:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)