
def registrar_usuario(base_de_datos):
    nombre = input("Ingrese el nombre del usuario: ")
    if nombre in base_de_datos:
        print("El usuario ya existe en la base de datos.")
        return
    
    constraseña = input("Ingrese la contraseña del usuario: ")
    
    base_de_datos[nombre] = {'contraseña': constraseña}
    print("Usuario registrado con exito.")

def iniciar_sesion(base_de_datos):
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre not in base_de_datos:
        print("Ese usuario no existe.")
        return
    
    contraseña = input("Ingrese su contraseña: ")
    if contraseña != base_de_datos[nombre]['contraseña']:
        print("Contraseña incorrecta.")
    else:
        print("Inicio de sesión exitoso.")


def mostrar_usuarios(base_de_datos):
    if not base_de_datos:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for nombre, info in base_de_datos.items():
            print(f"Nombre: {nombre}, contraseña: {info['contraseña']}")


base_de_datos = {}


while True:
    print("\n Menú ")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios registrados")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción que quiera: ")
    
    if opcion == '1':
        registrar_usuario(base_de_datos)
    elif opcion == '2':
        iniciar_sesion(base_de_datos)
    elif opcion == '3':
        mostrar_usuarios(base_de_datos)
    elif opcion == '4':
        print("¡Gracias, vuelva pronto!")
        break
    else:
        print("Error.Por favor, ingrese un número válido.")