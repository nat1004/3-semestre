Asistentes = {}

Asistentes.update({"1234":["1234","Juan",100.00]})
Asistentes.update({"2345":["2345","María",400.00]})
Asistentes.update({"3456":["3456","Brenda",350.00]})

print(Asistentes)

print("\nMenú de opciones:")
print("\t[A] Agregar")
print("\t[B] Buscar")
print("\t[E] Eliminar elemento")
print("\t[M] Modificar elemento")
print("\t[V] Ver datos")
print("\t[Q] Quitar todos los elementos de la lista")
print("\t[S] Salir")

while True:
    opcion=input("\n¿QUÉ DESEAS HACER?: ")

    if (not opcion.upper() in "ABEMVQS"):
        print("opcion no valida, intenta de nuevo")
        continue

    if (opcion.upper() == "S"):
        print("fin de la ejecucion")
        break

    if (opcion.upper() == "A"):
        socio = input("numero socio a agregar: ")

        if Asistentes.get(socio) == None:
            nombre = input("nombre del socio: ")
            aportacion = float(input("aportacion: "))
            Asistentes.update({socio:[socio, nombre, aportacion]})
            print("asistente agregado")
        else:
            print("asistente encontrado. no se puede repetir")
    
    if (opcion.upper() =="B"):
        socio = input("numero de socio a buscar: ")
        recuperado = Asistentes.get(socio)
        if recuperado == None:
            print("asistente no encontrado")
        else:
            Asistentes.pop(socio)
            print(f"{recuperado[0]}, {recuperado[1]}, {recuperado[2]}")

    if (opcion.upper() =="M"):
        socio = input("numero de socio a modificar: ")
        recuperado = Asistentes.get(socio)
        if recuperado == None:
            print("asistente no encontrado. no se puede modificar")
        else:
            print(f"datos actuales: {recuperado[0]}, {recuperado[1]}, {recuperado[2]}")
            nombre = input(("nuevo nombre del socio: "))
            aportacion = float(input("nueva aportacion: "))
            Asistentes.update({socio:[socio,nombre,aportacion]})
            print("asistente modificado")

    if (opcion.upper() == "E"):
        socio = input("numero de socio a eliminar: ")
        if Asistentes.get(socio)== None:
            print("asistente no encontrado. no se puede modificar")
        else:
            Asistentes.pop(socio)
            print("asistente eliminado")

    if (opcion.upper() =="V"):
        acumulado = 0.0
        print(f"elementos en la lista: {len(Asistentes)}")
        for v in Asistentes.values():
            print(f"{v[0]}, {v[1]}, {v[2]}")
            acumulado += v[2]
        print(f"acumulado: ${acumulado:,.2f}")

    if (opcion.upper() =="Q"):
        Asistentes.clear()
        print("todos los asistentes eliminados")
