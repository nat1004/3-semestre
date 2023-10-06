"""
cjto = set ([1,1,2,2,3])
print(cjto)

conjunto = {1,2,3,4}
print(conjunto)
print(type(conjunto))
print(f"la coleccion tiene {len(conjunto)} elementos")

conjunto = {1,2,3,4}
print(conjunto)

conjunto.add(5)
print(conjunto)

conjunto.add(5)
print(conjunto)

conjunto = {1,2,3,4}
print(conjunto)
conjunto.remove(2)
print(conjunto)

conjunto_A = {1,2,3,4,5}
conjunto_B = {4,5,6,7,8}

conjunto_C =conjunto_A.union(conjunto_B)
print(conjunto_A)
print(conjunto_B)
print(conjunto_C)

print("-----------------------")
print(conjunto_A)
conjunto_A.update(conjunto_B)
print(conjunto_A)

conjunto_A = {1,2,3,4,5}
conjunto_B = {4,5,6,7,8}

repetidos = conjunto_A.intersection(conjunto_B)
diferentes = conjunto_B.difference(conjunto_A)

print(repetidos)
print(diferentes)

conjunto_A = {1,2,3,4,5}
conjunto_C = conjunto_A
conjunto_D = conjunto_A.copy()
print(conjunto_C)
print(conjunto_D)

dias ={"lunes","martes","miercoles","jueves","viernes","sabado","domingo"}
for dia in  dias:
    print(dia)

dias = ("lun","mar","mie","jue","vie","sab","dom")
print(dias[3])
print(dias[2:4])
print(dias[2:])
print(dias[:2])
print(dias[-1])
print(dias[-2])
print(dias[-4:2])

numeros = (1,2,3,4,5,2,3,4,2,1,2)
valor_buscado = 3
primera_ocurrencia=numeros.index(valor_buscado)
print(f"se busco <{valor_buscado}>,  y se encontro en {primera_ocurrencia}")
print(f"el valor buscado esta {numeros.count(valor_buscado)} veces")


numeros_producto = (10,20,30)
nombres_producto = ("producto  10", "producto 20", "producto 30")
precios_producto = (100.20, 550.98, 2543.20)

producto_buscado = 40

if numeros_producto.count(producto_buscado)>0:
    indice = numeros_producto.index(producto_buscado)
    print(f"numero de producto: {numeros_producto[indice]}")
    print(f"nombre de producto: {nombres_producto[indice]}")
    print(f"precio de producto: ${precios_producto[indice]:,.2f}")
"""


"""
dias[2:4]=["Miercoles", "Jueves"]
print(dias)

dias[4:]=["Viernes"]
print(dias)

dias[0]="Lunes"
print(dias)

dias =["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print(dias)

dias.append("otro")
print(dias)

dias.insert(2,"otro mas")
print(dias)

print(dias.index("otro"))

print(dias[3])

dias.pop(8)
print(dias)

dias.remove("otro mas")
print(dias)

dias.pop()
print(dias)
dias.clear()
print(dias)

print(dias)

pelis_favoritas = "eyes wide shut;the godfather;the professional;the notebook"
favoritas = pelis_favoritas.split(';')
print(favoritas)
print(type(favoritas))

pelis_favoritas = "|eyes wide shut|the godfather|the professional|the notebook"
pelis_favoritas = "eyes wide shut;the godfather;the professional;the notebook"
favoritas = pelis_favoritas[1:-1].split('|')
print(favoritas)
print(type(favoritas))
"""
dias =["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

dias.sort()
print(dias)

dias.sort(reverse=True)
print(dias)

dias.reverse()
print(dias)