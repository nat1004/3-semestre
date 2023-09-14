print("\nMenú de opciones:")
print("\t[A] Agregar")
print("\t[B] Buscar")
print("\t[E] Eliminar elemento")
print("\t[V] Ver lista")
print("\t[Q] Quitar todos los elementos de la lista")
print("\t[S] Salir")

Asistentes=[]

while True:
 
 opcion=input("\n¿QUÉ DESEAS HACER?: ")
 
 if (not opcion.upper() in "ABEVQS"):
   print("Opción no válida, intenta de nuevo.")
   continue
 
 if (opcion.upper()=="S"):
   print("Fin de la ejecución.")
   break
 
 if (opcion.upper()=="A"):
   while True:
    asistente=input("Asistente a agregar: ")
    if (asistente==""):
      break 
    if Asistentes.count(asistente)==0: 
      Asistentes.append(asistente)
      print("Asistente agregado.")
    else:
      print("Asistente encontrado. No se puede repetir.")

 if (opcion.upper()=="B"):
   asistente=input("Asistente a buscar: ")
   if Asistentes.count(asistente)==0:
     print("Asistente no encontrado.")
   else:
     posicion=Asistentes.index(asistente)
     print(f"Asistente encontrado. Índice {posicion}")

 if (opcion.upper()=="E"):
   asistente=input("Asistente a eliminar: ")
   if Asistentes.count(asistente)==0:
     print("Asistente no encontrado. No se puede eliminar.")
   else:
     Asistentes.remove(asistente)
     print("Asistente eliminado.")
 
 if (opcion.upper()=="V"):
   print(f"Elementos en la lista: {len(Asistentes)} ")
   for a in Asistentes:
     print("-->", a)
     
 if (opcion.upper()=="Q"):
   Asistentes.clear()
   print("Todos los asistentes eliminados.")
