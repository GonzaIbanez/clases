from Paquete_entrega import Cliente
from Paquete_entrega import LocalCompras

local_compras = LocalCompras()

cliente1 = Cliente("Lautaro", "Zarate", "lau@outlook.com", "yapeyu 456")
cliente2 = Cliente("Jorge", "Lazaro", "Jorg1@outlook.com", "rascacielos 3000")

local_compras.agregar_cliente(cliente1)
local_compras.agregar_cliente(cliente2)

local_compras.mostrar_clientes()