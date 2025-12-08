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
    listaAux = []

    for num in lista:

        if len(listaAux) == 0:
            listaAux.append(num)

        elif num > listaAux[len(listaAux)-1]:
            # Tambien funciona listaAux[-1] para mostrar el ultimo numero agregado
            listaAux.append(num)
            
    print(listaAux)

secuenciaCreciente(lista)
print("========================================================================")