print("========================================================================")
print("Rotar una lista k posiciones a la derecha")
print("Dada una lista de números enteros y un número k,")
print("rota la lista k posiciones hacia la derecha.")
print("")
print("Ejemplo:")
print("lista = [1, 2, 3, 4, 5]")
print("k = 2")
print("Salida: [4, 5, 1, 2, 3]")
print("")
print("Restricciones:")
print("- No usar slicing")
print("- No usar funciones avanzadas")
print("- No usar collections")
print("- Solo ciclos, índices y variables auxiliares")
print("- Puedes usar una lista auxiliar")
print("========================================================================")
lista = [1, 2, 3, 4, 5]
k = 2

def rotarListaIndice(lista, indice):
    tamanio = len(lista)
    listaR = []
    aux = 0
    for i in range(indice):
        listaR.append(lista[-1+aux])
        aux=-1

    for j in range(tamanio - len(listaR)):
        listaR.append(lista[j])
    
    print(listaR)

rotarListaIndice(lista, k)

print("========================================================================")

