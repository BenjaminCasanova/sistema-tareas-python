


tareas = []



# Función para agregar una tarea
def agregar_tarea():

    nombre = input("\nIngrese el nombre de la tarea: ").strip()

    if nombre == "":
        print(" El nombre de la tarea no puede estar vacío.")
        return

    tarea = {
        "nombre": nombre,
        "estado": "Pendiente"
    }

    tareas.append(tarea)

    print("La tarea fue agregada correctamente.")

def listar_tareas():

    if len(tareas) == 0:
        print("\n⚠ No existen tareas registradas.")
        return

    print("\n========== LISTA DE TAREAS ==========")

    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea['nombre']} - {tarea['estado']}")


def completar_tarea():

    if len(tareas) == 0:
        print("\n⚠ No existen tareas para completar.")
        return

    listar_tareas()

    try:

        numero = int(input("\nSeleccione el numero de la tarea: "))

        if numero < 1 or numero > len(tareas):
            print(" Número de tarea invalido.")
            return

        if tareas[numero - 1]["estado"] == "completada":
            print("⚠ Esa tarea ya está completada.")
            return

        tareas[numero - 1]["estado"] = "completada"

        print("Tarea completada correctamente.")

    except ValueError:
        print("Debe ingresar un numero válido.")


def eliminar_tarea():

    if len(tareas) == 0:
        print("\n⚠ No existen tareas para eliminar.")
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
            completar_tarea()

            print("Hasta luego.")
            break

        else:
            print("Opción inválida.")


            print("Opción invalida.")

menu()