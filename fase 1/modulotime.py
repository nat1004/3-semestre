import time
import datetime
segundos = int(input("cantidad de segundos a esperar:\n"))
time.sleep(segundos)
print(f"han trascurrido por lo menos {segundos} segundos")

horainicial = time.time()
for termino in range(10):
    time.sleep(segundos)
    
print("proceso simulado concluido")
duracion = time.time() - horainicial
print(f"la duracion del proceso simulado fue de {duracion:.4f} segundos")

hora = datetime.time(10,20,30)
print(f"el tipo de objeto de la hora es {type(hora)}")
print(f"la hora es {hora}")
print(f"la hora de {hora} es {hora.hour}")
print(f"el minuto de {hora} es {hora.minute}")
print(f"el segundo de {hora} es {hora.second}")
print(f"el microsegundo de {hora} es {hora.microsecond}")

fecha_actual = datetime.date.today()
print(f"el tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"la fecha actual es  {fecha_actual}")
print(f"el año actual es {fecha_actual.year}")
print(f"el mes actual es {fecha_actual.month}")
print(f"el dia actual es {fecha_actual.day}")

fecha_capturada = input("dime una fecha (dd/mm/aaaa): \n")
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
print(type(fecha_capturada))
print(type(fecha_procesada))
print(f"la fecha capturada se transformo a {fecha_procesada}")

print(f"de entrada, tenemos el valor {fecha_procesada} en la variable con el tipode dato especializado")

print(f"el mismo valor lo podemos presentar en el formato dd/mm/aaaa {fecha_procesada.strftime('%d/%m/%Y')}")
print(f"o tambien en formato mm/dd/aaaa: {fecha_procesada.strftime('%m/%d/%Y')}")

cant_dias = int(input(f"dime laa cantidad de dias a adelantar respecto a {fecha_procesada}: "))
nueva_fecha = fecha_procesada + datetime.timedelta(days=+cant_dias)

print(f"la nueva fecha es {nueva_fecha}")