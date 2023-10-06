import random

print(f"obteniento un numero entero aleatorio que puede ir del 0 al 19: {random.randrange(20)}")
print(f"obteniento un numero entero aleatorio par que puede ir del 2 al 20 {random.randrange(2,21,2)}")
print(f"obteniento un numero entero aleatorio que puede ir del 0 hasta el 20: {random.randint(1,20)}")
print(f"obteniento un valor numerico entre 0.0 y 1.0 inclusive: {random.random()}")

listadeprueba = [10,20,30,40,15,25,35,45]
print(f"la lista de prueba es {listadeprueba}")
print(f"el valor seleccionado aleatoriamente de la linea anterior es {random.choice(listadeprueba)}")
random.shuffle(listadeprueba)
print(f"la lista ya 'perturbada/barajada' es {listadeprueba}")