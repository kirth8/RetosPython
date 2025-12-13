print("========================================================================")
print("Mover los ceros al final")
print("Dada una lista de números enteros, debes mover todos los ceros al final de la lista, " \
"manteniendo el orden relativo de los demás números.")
print("Ejemplo:\nlista = [0, 1, 0, 3, 12]\n\nSalida: [1, 3, 12, 0, 0]\n")
print("Restricciones:\n- No usar sort() ni sorted()\n- No usar listas por comprensión")
print("- No usar funciones avanzadas\n- Solo ciclos, comparaciones y listas auxiliares\n- Mantener " \
"el orden de los números no cero")
print("========================================================================")
lista = [0, 1, 0, 3, 12]
listaR = []

def cerosFinal(lista, listaR):
    contador = 0

    for num in lista:
        if num != 0:
            listaR.append(num)
        else:
            contador += 1
    
    for i in range(contador):
        listaR.append(0)

    print(listaR)

cerosFinal(lista, listaR)
print("========================================================================")