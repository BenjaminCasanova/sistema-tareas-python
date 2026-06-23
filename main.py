def menu():
  while True:
    print("/n ---Menu---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
            print("Función agregar tarea proximamente")
        elif opcion == "2":
            print("Función listar tareas proximamente")
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción invalida")

menu()
