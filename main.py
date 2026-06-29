# Sistema de Registro de Tareas Personales
# Tarea Finalizada - Evidencia 6

# Lista donde se almacenan las tareas
tareas = []


# Ffuncionn que permite agregar una nueva tarea
def agregar_tarea():

    nombre = input("\nIngrese el nombre de la tarea: ").strip()

    if nombre == "":
        print("El nombre de la tarea no puede estar vacío.")
        return

    tarea = {
        "nombre": nombre,
        "estado": "pendiente"
    }

    tareas.append(tarea)

    print("Tarea agregada correctamente.")


# Funcion que muestra todas las tareas registradas
def listar_tareas():

    if len(tareas) == 0:
        print("\nNo existen tareas registradas.")
        return

    print("\n========== LISTA DE TAREAS ==========")

    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea['nombre']} - {tarea['estado']}")


# Funcion que cambia el estado de una tarea a completada
def completar_tarea():

    if len(tareas) == 0:
        print("\nNo existen tareas para completar.")
        return

    listar_tareas()

    try:

        numero = int(input("\nSeleccione el numero de la tarea: "))

        if numero < 1 or numero > len(tareas):
            print("Número de tarea invalido.")
            return

        if tareas[numero - 1]["estado"] == "Completada":
            print("Esa tarea ya está completada.")
            return

        tareas[numero - 1]["estado"] = "Completada"

        print("Tarea completada correctamente.")

    except ValueError:
        print("Debe ingresar un número válido.")


# Funcion que elimina una tarea de la lista
def eliminar_tarea():

    if len(tareas) == 0:
        print("\nNo existen tareas para eliminar.")
        return

    listar_tareas()

    try:

        numero = int(input("\nSeleccione el numero de la tarea que desea eliminar: "))

        if numero < 1 or numero > len(tareas):
            print("Número de tarea invalido.")
            return

        tarea = tareas.pop(numero - 1)

        print(f"La tarea '{tarea['nombre']}' fue eliminada correctamente.")

    except ValueError:
        print("Debe ingresar un número válido.")


# Funcion principal del sistema
def menu():

    while True:

        print("\n===================================")
        print(" SISTEMA DE REGISTRO DE TAREAS")
        print("===================================")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            listar_tareas()

        elif opcion == "3":
            completar_tarea()

        elif opcion == "4":
            eliminar_tarea()

        elif opcion == "5":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida.")


menu()