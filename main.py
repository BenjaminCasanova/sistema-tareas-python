


tareas = []

def agregar_tarea():

    nombre = input("Ingrese el nombre de la tarea: ").strip()

    if nombre == "":
        print("El nombre de la tarea no puede estar vacio.")
        return

    tarea = {
        "nombre": nombre,
        "estado": "Pendiente"
    }

    tareas.append(tarea)

    print("La tarea fue agregada correctamente.")

# Función para listar tareas
def listar_tareas():

    if len(tareas) == 0:
        print("\nNo existen tareas registradas.")
        return

    print("\n========== TAREASS ==========")

    for i in range(len(tareas)):
        print(f"{i+1}. {tareas[i]['nombre']} - {tareas[i]['estado']}")

# Menú principal
def menu():

    while True:

        print("\n===================================")
        print(" SISTEMA DE REGISTRO DE TAREAS")
        print("===================================")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            agregar_tarea()

        elif opcion == "2":

            listar_tareas()

        elif opcion == "3":

            print("Hasta luego.")
            break

        else:

            print("Opción invalida.")

# Inicio del programa
menu()
