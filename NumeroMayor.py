print("========================================================================\n")
print("Encontrar el número mayor sin usar max()\n")
print("Dada una lista de enteros, devuelve el número más grande.\nEjemplo:\n\n")
print("input: [3, 9, 1, 7, 4]\n\noutput: 9\n\n")
print("Restricciones:\n-No usar max()\n-No ordenar la lista\n-Solo ciclos, comparaciones y variables")
print("========================================================================\n")

lista = [3, 9, 1, 7, 4]

def numeroMayor(lista):
    aux = lista[0] #No lo pongo un un valor de 0 inicial porque puede haber numero negativos
    print(aux)
    for num in lista:
        if num > aux:
            aux = num

    print("\nResultado: ", aux)

numeroMayor(lista)

print("\n========================================================================\n")