import os
import sys

lista = list()
for numero in range(1,1001):
    lista.append(numero)
    
consumo_lista = sys.getsizeof(lista)
print(f"la lista tiene {len(lista)} elementos, y tiene un tamaño de {consumo_lista} bytes")

tupla = tuple(lista)
consumo_tupla= sys.getsizeof(lista)
print(f"la tupla tiene {len(tupla)} elementos, y tiene un tamaño de {sys.getsizeof(tupla)} bytes")

proporcion = (consumo_tupla / consumo_lista)  * 100
print(f"la version en tupla de los datos tiene un consumo del {proporcion:.2f}% respecto a la version en una")

print(f"el directorio actual de trabajo es {os.getcwd()}")

for raiz, dirs, archivos in os.walk(".", topdown=False):
    for nombre in archivos:
        print(os.path.join(raiz, nombre))
    for nombre in dirs:
        print(os.path.join(raiz, nombre))