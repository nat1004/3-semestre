peliculas={
 10:"The Godfather",
 20:"Jurassic Park",
 30:"Ex-Machina",
 40:"The Notebook"
}
"""
print(len(peliculas))
print(peliculas.keys())
print(peliculas.values())

print(peliculas[40])
print(peliculas.get(40))

print(peliculas.items())
"""

print(peliculas)

peliculas[50] = "starwars"

peliculas.update({60:"unknown"})

print(peliculas)

peliculas[60] = "casino royale"

print(peliculas)

peliculas.popitem()
print(peliculas)

peliculas.pop(20)
print(peliculas)

del peliculas[30]
print(peliculas)

for llave in peliculas:
    print(llave)

for llave in peliculas:
    print(peliculas[llave])

for llave in peliculas.keys():
    print(llave)

for valor in peliculas.values():
    print(valor)

for llave, valor in peliculas.items():
    print(f"a la llave {llave} le corresponde el valor {valor}")

print(peliculas)
lo_mismo = peliculas
peliculas[80] = "fifth element"
print(lo_mismo)

peliculas_1 = peliculas.copy()
peliculas_1[90] = "toy story"
print(peliculas)
print(peliculas_1)

peliculas_2 = dict(peliculas)
peliculas_2[90] = "sharknado"

print(peliculas)
print(peliculas_2)

productos = {
    10:{
        "id":10,
        "desc":"producto 10",
        "precio":2992.45
    },
    20:{
        "id":20,
        "desc":"producto 20",
        "precio":834.55
    }
}

referencia = 20

if referencia in productos.keys():
    datos = productos.get(referencia)
    print(datos)
    print(datos["id"])
    print(datos["desc"])
    print(datos["precio"])

operaciones_a = {
    12922:"cliente 1",
    27728:"cliente 2",
    28939:"cliente 3"
}

operaciones_b = {
    12922:"cliente 1",
    73772:"cliente 4",
    46677:"cliente 5"
}

operaciones_c = operaciones_a.copy()

for llave,valor in operaciones_b.items():
    if (not llave in operaciones_c.keys()):
        operaciones_c[llave] = valor

print(operaciones_c)
print(len(operaciones_c))