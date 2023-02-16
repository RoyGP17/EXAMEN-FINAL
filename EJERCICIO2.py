# Definimos la clase Nodo para representar los nodos de la pila
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definimos la clase Pila para representar el historial de tareas pendientes
class Pila:
    def __init__(self):
        self.tope = None   # El tope de la pila (último nodo)
        self.tamaño = 0    # El tamaño de la pila (cantidad de nodos)

    # Agrega un nuevo nodo al inicio de la pila
    def agregar(self, dato):
        nuevoNodo = Nodo(dato)
        nuevoNodo.siguiente = self.tope
        self.tope = nuevoNodo
        self.tamaño += 1

    # Elimina el último nodo de la pila
    def eliminar(self):
        if self.tope is not None:
            self.tope = self.tope.siguiente
            self.tamaño -= 1

    # Muestra todos los nodos de la pila en orden inverso al que se agregaron
    def mostrar(self):
        actual = self.tope
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

# Creamos una nueva instancia de Pila para representar el historial de tareas pendientes
historialTareas = Pila()

# Bucle infinito para mostrar un menú al usuario y procesar su elección
def menu():
    while True:
        #Menu de opciones presentadas al usuario
        print("\n1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar historial")
        print("4. Mostrar cantidad de tareas")
        print("5. salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # Si el usuario elige "Agregar tarea", pedimos que ingrese la tarea y la agregamos al historial
            tarea = input("Ingrese la tarea que desea agregar: ")
            historialTareas.agregar(tarea)
        elif opcion == 2:
            # Si el usuario elige "Eliminar tarea", eliminamos la última tarea del historial
            historialTareas.eliminar()
        elif opcion == 3:
            # Si el usuario elige "Mostrar historial de tareas", mostramos todas las tareas en orden inverso al que se agregaron
            print("\nHistorial de tareas:")
            historialTareas.mostrar()
        elif opcion == 4:
            # Si el usuario elige "Mostrar cantidad de tareas", mostramos la cantidad total de tareas en el historial
            print("\nCantidad de tareas pendientes:", historialTareas.tamaño)
        elif opcion == 5:
            # Si el usuario elige "Salir", salimos del bucle y terminamos el programa
            break
        else:
            # Si el usuario ingresa una opción inválida, le avisamos y le pedimos que elija de nuevo
            print("Opción incorrecta! Intente nuevamente.")
menu()