print("========================================================================")
print("Encontrar la subsecuencia creciente más larga (LIS simplificada)")
print("Dada una lista de números enteros, encuentra la subsecuencia estrictamente creciente más" \
" larga, pero en su versión simplificada:")
print("Ejemplo:\n\nLista = [3, 1, 2, 5, 4, 7]\n\nLa subsecuencia creciente más larga es: [1, 2, 5, 7]\n(longitud 4)\n")
print("Restricciones:")
print("- No usar librerías externas.")
print("- No usar métodos avanzados como programación dinámica.")
print("- No ordenar la lista.")
print("- Solo ciclos, comparaciones y variables auxiliares.")
print("- Puedes recorrer la lista las veces que necesites.")
print("- No necesitas resolver la versión completa del LIS, solo necesitas encontrar una " \
"subsecuencia creciente válida y lo más larga posible usando lógica básica.")
print("========================================================================")
lista = [3, 1, 2, 5, 4, 7]

def secuenciaCreciente(lista):
    aux = lista[0]
    listaR = []
    contador = 0

    for num in lista:
        if aux < num:
            aux = num
            listaR.append(aux)
            contador += 1
        elif num < aux and listaR[contador-1] > num:
            # aux = num
            listaR.append(num)
            contador += 1
    print(listaR)

secuenciaCreciente(lista)
print("========================================================================")