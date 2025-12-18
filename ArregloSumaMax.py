print("========================================================================")
print("Encontrar el subarreglo con suma máxima (versión básica)")
print("Dada una lista de números enteros (pueden ser positivos y negativos),")
print("encuentra el subarreglo contiguo cuya suma sea la mayor posible.")
print("")
print("Ejemplo:")
print("lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]")
print("Salida: 6  # subarreglo [4, -1, 2, 1]")
print("")
print("Restricciones:")
print("- No usar librerías")
print("- No usar programación dinámica explícita")
print("- No usar funciones avanzadas")
print("- Solo ciclos, comparaciones y variables auxiliares")
print("- Puedes recorrer la lista varias veces")
print("========================================================================")

lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def sumaMaxArreglo(lista):
    suma_actual = 0
    suma_maxima = lista[0]

    for num in lista:
        suma_actual = suma_actual + num

        if suma_actual > suma_maxima:
            suma_maxima = suma_actual

        if suma_actual < 0:
            suma_actual = 0

    print("Suma máxima:", suma_maxima)

sumaMaxArreglo(lista)
print("========================================================================")
