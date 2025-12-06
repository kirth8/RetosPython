print("========================================================================")
print("Encontrar el segundo número mayor de una lista")
print("Dada una lista de enteros, encuentra el segundo número más grande.")
print("Ejemplo:\n")
print("input:  [10, 4, 7, 20, 15]\noutput: 15\n")
print("Restricciones:\n-No usar sorted()\n-No usar max()\n-No ordenar la lista\n-Solo ciclos, " \
"comparaciones y variables auxiliares\n-Puedes recorrer la lista las veces que necesites, pero intenta hacerlo en una sola pasada si puedes")

print("========================================================================")
lista = [10, 4, 20, 15]

def encontrarMayorSegundo(lista):
    aux = lista[0]
    auxR = 0

    for num in lista:
        if num > aux:
            auxR = aux
            aux = num
        elif num > auxR and num != aux:
            auxR = num

    
    print("Numero Mayor= ", aux, ", y Segundo Mayor= ", auxR)

print("Lista = ", lista)

encontrarMayorSegundo(lista)

print("========================================================================")