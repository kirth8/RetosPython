print("========================================================================")
print("Encontrar el elemento que aparece un número impar de veces")
print("Dada una lista de enteros, todos los números aparecen un número par de veces")
print("excepto uno solo, que aparece un número impar de veces.")
print("")
print("Tu tarea es encontrar ese número.")
print("")
print("Ejemplo:")
print("lista = [2, 3, 2, 4, 4, 3, 5]")
print("Salida: 5")
print("")
print("Restricciones:")
print("- No usar collections")
print("- No usar funciones avanzadas")
print("- Puedes usar diccionarios o solo ciclos y variables auxiliares")
print("- Recorrer la lista")
print("========================================================================")
lista = [2, 3, 2, 4, 4, 3, 5]


def encontrarElementoImpar(lista):
    aux = []

    for num in lista:
        if num in aux:
            aux.remove(num)
        else:
            aux.append(num)

    print(f"El numero es: {aux[0]}")

            
encontrarElementoImpar(lista)

print("========================================================================")
