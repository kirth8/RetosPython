print("========================================================================")
print("Encontrar el primer número repetido")
print("Dada una lista de enteros, encuentra el primer número que aparece repetido (es decir, " \
"el primero que aparece por segunda vez cuando recorres la lista de izquierda a derecha).")
print("Ejemplo:\n")
print("Lista: [3, 1, 4, 2, 5, 1, 4, 3]\n")
print("Salida: 1\n")
print("Restricciones:")
print("- No usar set()\n- No usar collections\n- No usar funciones avanzadas\n- Solo:")
print("-- ciclos\n-- comparaciones\n-- variables auxiliares\n-- diccionarios o listas creadas por ti")
print("========================================================================")

lista = [3, 1, 4, 2, 5, 1, 4, 3]

def NumeroRepetido(lista):
    vistos = {} 

    for num in lista:
        if num in vistos:
            print("El primer número repetido es:", num)
            return
        else:
            vistos[num] = 1

    print("No hay números repetidos")

NumeroRepetido(lista)


print("========================================================================")
