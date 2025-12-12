print("========================================================================")
print("Encontrar el primer número que NO se repite")
print("Dada una lista de enteros, debes encontrar el primer número que aparece exactamente" \
" una sola vez, recorriendo la lista de izquierda a derecha.")
print("Ejemplo:\nLista: [4, 5, 1, 2, 1, 4, 2, 7, 5]")
print("- Los repetidos son: 4, 5, 1, 2\n- l primer número que NO se repite es: 7\n")
print("Salida: 7\n")
print("Restricciones:")
print("- No usar collections.Counter\n- No usar set()\n- No usar funciones avanzadas\n- Solo:")
print("-- ciclos\n-- comparaciones\n-- diccionarios o listas creadas por ti\n-- variables auxiliares")
print("========================================================================")
lista = [4, 5, 1, 2, 1, 4, 2, 7, 5]

def encontrarNoRepetido(lista):
    conteo = {}

    for num in lista:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1

    for num in lista:
        if conteo[num] == 1:
            return num

resultado = encontrarNoRepetido(lista)
print("Primer número que NO se repite:", resultado)

print("========================================================================")
