tareas = []


# Función para agregar una tarea
def agregar_tarea():

    nombre = input("\nIngrese el nombre de la tarea: ").strip()

    if nombre == "":
        print("El nombre de la tarea no puede estar vacio.")
        return

    tarea = {
        "nombre": nombre,
        "estado": "Pendiente"
    }

    tareas.append(tarea)

    print("Tarea agregada correctamente.")


def listar_tareas():

    if len(tareas) == 0:
        print("\nNo existen tareas registradas.")
        return

    print("\n= TAREAS =")

    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea['nombre']} - {tarea['estado']}")



def completar_tarea():

    if len(tareas) == 0:
        print("\nNo existen tareas para completar.")
        return

    listar_tareas()

    try:

        numero = int(input("\nSeleccione el número de la tarea: "))

        if numero < 1 or numero > len(tareas):
            print("Número de tarea inválido.")
            return

        tareas[numero - 1]["estado"] = "Completada"

        print("La tarea fue marcada como completada.")

    except ValueError:
        print("Debe ingresar un número válido.")


def menu():

    while True:

        print("\n========================================")
        print("   SISTEMA DE REGISTRO DE TAREAS")
        print("========================================")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            listar_tareas()

        elif opcion == "3":
            completar_tarea()

        elif opcion == "4":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida.")



menu()