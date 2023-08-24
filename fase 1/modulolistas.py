lista_original = [3,4,2]
print(lista_original)

lista_original.sort()
print(lista_original)

lista_original2 = [23, 10, 30, 5]
lista_ordenada = sorted(lista_original2)

print(f"lista original = {lista_original2}, y la version ordenada es {lista_ordenada}")

lista_base = ["a",  "b", "c", "d"]
copia = lista_base

copia_2 = lista_base.copy()
copia_3 = list(lista_base)
copia_4 = lista_base[:]
print(copia_2)
print(copia_3)
print(copia_4)

lista_uno = [10, 20, 30, 40, 50]

lista_resultante = []
for valor in lista_uno:
    lista_resultante.append(valor * 2)
print(F"resultado = {lista_resultante}")

lista_resultante = [valor * 2 for valor in lista_uno]
print(f"resultado = {lista_resultante}")

secuencia_entera = [valor for valor in range(1,101)]
print(secuencia_entera)

lista_base = ["a",  "b", 1, "c", 2, 3, 5]
lista_destino = [valor for valor in lista_base if(isinstance(valor, int))]
print(lista_destino)