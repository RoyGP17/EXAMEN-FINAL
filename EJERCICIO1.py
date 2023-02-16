'''1. Crea un programa en Python que simule una lista de compras.
El programa debe permitir al usuario agregar productos al final de la lista,
eliminar productos del inicio de la lista y mostrar todos los productos en la lista en orden de compra.'''

print("========== Programa Compras ==========")
# Definimos la clase Nodo para representar los nodos de la lista simple
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definimos la clase ListaSimple para representar la lista de compras
class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None   # La cabeza de la lista (primer nodo)
        self.tamaño = 0      # El tamaño de la lista (cantidad de nodos)

    # Agrega un nuevo nodo al final de la lista
    def agregar(self, dato):
        nuevoNodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo
        self.tamaño += 1

    # Elimina el primer nodo de la lista
    def eliminar(self):
        if self.cabeza is not None:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1

    # Muestra todos los nodos de la lista en orden de compra
    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

# Creamos una nueva instancia de ListaSimple para representar la lista de compras
listaDeCompras = ListaEnlazadaSimple()

# Bucle infinito para mostrar un menú al usuario y procesar su elección
def menu():
    while True:
        # Menu de opciones presentadas al usuario
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar lista de compras")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # Si el usuario elige "Agregar producto", pedimos el nombre del producto y lo agregamos a la lista
            producto = input("Ingrese el nombre del producto que desea agregar: ")
            listaDeCompras.agregar(producto)
        elif opcion == 2:
            # Si el usuario elige "Eliminar producto", eliminamos el primer producto de la lista
            listaDeCompras.eliminar()
        elif opcion == 3:
            # Si el usuario elige "Mostrar lista de compras", mostramos todos los productos de la lista en orden de compra
            print("\nLista de compras:")
            listaDeCompras.mostrar()
        elif opcion == 4:
            # Si el usuario elige "Salir", salimos del bucle y terminamos el programa
            break
        else:
            # Si el usuario ingresa una opción inválida, le avisamos y le pedimos que elija de nuevo
            print("Opción incorrecta! Intente nuevamente.")
menu()