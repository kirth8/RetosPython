print("========================================================================\n")
print("Contar cuántas veces aparece un número en una lista")
print("Dado un arreglo de enteros y un número objetivo, devuelve cuántas veces aparece ese número.")
print("Ejemplo:\n\ninput: lista = [1, 2, 2, 3, 2, 4], objetivo = 2\n\noutput: 3")
print("\nRestricciones:\n-No usar .count()\n-Solo ciclos, variables y condicionales\n-No modificar la lista")
print("========================================================================\n\n")

lista = [1, 2, 2, 3, 2, 4]
objetivo = 2

def contarNumero(lista, objetivo):
    out = 0
    for num in lista:
        if num == objetivo:
            out += 1

    print("Respuesta: ", out, "\n\n")

contarNumero(lista, objetivo)