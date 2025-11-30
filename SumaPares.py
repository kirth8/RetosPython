print("========================================================================")
print("Dado un arreglo de enteros, devuelve la suma de todos los números pares.")
print("Restricciones:\n-No usar funciones avanzadas como sum() con filtros.\n"
"-Solo ciclos, condicionales y operaciones básicas.")
print("input: [1, 2, 3, 4, 6]")
print("output: 12   # (2 + 4 + 6)")
print("========================================================================\n \n")

intArreglo = [1, 2, 3, 4, 6]


def sumaPar( intArreglo):
    outSuma = 0
    for num in intArreglo:
        if (num%2 == 0):
            outSuma += num

    print("La respuesta es: ", outSuma)


sumaPar(intArreglo)

    
print("========================================================================\n \n")