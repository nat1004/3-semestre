import numpy as np
"""
lista = [25,12,15,66,12.5]
vector = np.array(lista)
print(vector)

lista_de_lista = [[2,0],[3,0],[3,1],[5,0],[5,1],[5,2]]
print(lista_de_lista)
print()
a = np.array([[2,0],[3,0],[3,1],[5,0],[5,1],[5,2]])
print("el contenido del array de numpy es: ")
print(a)

print(f"y es un obeto de tipo: {type(a)}")


a[:,0] = 15
print(a)
print()
a[:,1] = 30
print(a)

arreglo2 = np.zeros(shape=(2,4), dtype= int)
print(arreglo2)
print(f"\nlas dimensiones del arreglo son {arreglo2.shape}")

arreglo_aleatorio = np.random.randint(1,11, size= 10)
print(arreglo_aleatorio)

matriz_aleatorio = np.random.randint(1,11, size= (2,4))
print(matriz_aleatorio)

dos_en_dos =np.arange(10,25,2)
print(dos_en_dos)

print(f"\nlas dimensiones de la estructura resultantes son: {dos_en_dos.shape}")
lista = [10, "abc", 20]
print(lista)
print(*[type(elemento) for elemento in lista], sep="\n")

arreglo = np.array([10, "abc", 20])
print(arreglo)
print(*[type(elemento) for elemento in lista], sep="\n")

lista = [10,15,20,25]
print(lista)
print(f"\n{lista * 2}")

arreglo = np.array([10,15,20,25])
print(arreglo)
print()
print(arreglo * 2)

matrizA = np.random.randint(1,300, size=(5,10))
matrizB = np.random.randint(1,300, size=(5,10))

print(f"matriz A\n{matrizA}")
print("\nX\n")
print(f"matriz B\n{matrizB}")
print("\n=\n")
print(matrizA * matrizB)

arreglo_uni = np.array([1,2,3,4,5,6,7,8,9])

filtro = arreglo_uni < 5
print(filtro)
resultado = arreglo_uni[filtro]
print()
print(resultado)

matriz_ejemplo = np.random.randint(1,300, size=(2,5))
print(matriz_ejemplo)
print()
filtro = matriz_ejemplo > 100
print(filtro)
print()
resultado = matriz_ejemplo[filtro]
print(resultado)"""

datos = np.random.randint(1,200, size=(18,))
print("los datos son: ")
print(datos)
"""
minimo = datos.min()
maximo = datos.max()

print(f"\nlos datos tienen un rango de {maximo - minimo}, abarcando desde el {minimo} hasta el {maximo}")

primer_cuartil = np.percentile(datos, 25)
mediana = np.median(datos)
tercer_cuartil = np.percentile(datos, 75)
print(f"\nla mediana de los datos es igual a {mediana}")
print(f"el primer cuartil es igual a {primer_cuartil}, mientras que el tercer cuartil es igual a {tercer_cuartil}")
print(f"con rango intercuartil = {primer_cuartil} a {tercer_cuartil} o {tercer_cuartil - primer_cuartil}")

media = datos.mean()
desviacion_estandar = datos.std()
varianza = datos.var()

print(f"\nlos datos poseen una media aritmetica de {media: .4f}, con una varianza de {varianza: .4f} y una desvicion estandar de {desviacion_estandar: .4f}")
"""

media = np.mean(datos)
desviacion_estandar = np.std(datos)
varianza = np.var(datos)

print(f"\nlos datos poseen una media aritmetica de {media: .4f}, con una varianza de {varianza: .4f} y una desvicion estandar de {desviacion_estandar: .4f}")
