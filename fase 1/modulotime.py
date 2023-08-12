import time
segundos = int(input("cantidad de segundos a esperar:\n"))
time.sleep(segundos)
print(f"han trascurrido por lo menos {segundos} segundos")

horainicial = time.time()
for termino in range(10):
    time.sleep(segundos)
    
print("proceso simulado concluido")
duracion = time.time() - horainicial
print(f"la duracion del proceso simulado fue de {duracion:.4f} segundos")