# Lista donde se almaceranan las tareas
tareas = []

# Función para agregar una tarea
def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")

    if nombre.strip() == "":
        print("El nombre de la tarea no puede estar vacío.")
        return

    tarea = {
        "nombre": nombre,
        "estado": "Pendiente"
    }

    tareas.append(tarea)
    print("Tarea agregada correctamente.")

# Función para listar las tareas
def listar_tareas():
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    print("\n===== LISTA DE TAREAS =====")

    for i in range(len(tareas)):
        print(f"{i + 1}. {tareas[i]['nombre']} - {tareas[i]['estado']}")


def menu():

    while True:

        print("\n===== SISTEMA DE REGISTRO DE TAREAS =====")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            listar_tareas()

        elif opcion == "3":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opcion invalida.")


menu()
