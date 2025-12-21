print("========================================================================")
print("Detectar si una lista tiene elementos consecutivos")
print("Dada una lista de números enteros,")
print("verifica si contiene al menos una secuencia")
print("de 3 números consecutivos (en cualquier posición).")
print("")
print("Ejemplo 1:")
print("lista = [10, 3, 4, 5, 20]")
print("Salida: True   # 3,4,5")
print("")
print("Ejemplo 2:")
print("lista = [1, 2, 4, 6, 8]")
print("Salida: False")
print("")
print("Ejemplo 3:")
print("lista = [7, 8, 9]")
print("Salida: True")
print("")
print("Restricciones:")
print("- No usar set()")
print("- No usar sorted()")
print("- No usar collections")
print("- Solo ciclos, comparaciones y variables auxiliares")
print("- Puedes recorrer la lista varias veces")
print("========================================================================")

lista1 = [10, 3, 4, 5, 20]
lista2 = [1, 2, 4, 6, 8]
lista3 = [7, 8, 9]

def verificarSecuenciaConsecutiva(lista):
    for num in lista:
        encontrado1 = False
        encontrado2 = False

        for otro in lista:
            if otro == num + 1:
                encontrado1 = True
            if otro == num + 2:
                encontrado2 = True

        if encontrado1 and encontrado2:
            print("Es consecutiva por:", num, num + 1, num + 2)
            return

    print("No es consecutiva")



verificarSecuenciaConsecutiva(lista1)

print("========================================================================")
