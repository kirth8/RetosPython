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
    aux = lista[0]
    contador = 0
    listaR = []
    for num in lista:
        if num >= aux:
            aux=num
            contador +=1
            listaR.append(aux)
        else:
            print("No es consecutiva")
            return

    print("Si es consecutiva")


verificarSecuenciaConsecutiva(lista1)

print("========================================================================")
